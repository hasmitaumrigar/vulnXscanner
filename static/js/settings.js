// Settings Management JavaScript

// Default thread configurations
const DEFAULT_SETTINGS = {
    portScanner: {
        threadsDefault: 100,
        threadsExtended: 500
    },
    subdomainFinder: {
        threadsNormal: 200,
        threadsDeep: 800
    },
    directoryFinder: {
        threadsNormal: 150,
        threadsDeep: 800
    },
    databaseScanner: {
        threads: 6
    }
};

// Storage key for localStorage
const SETTINGS_STORAGE_KEY = 'vulnx_scanner_settings';

/**
 * Initialize tab navigation
 */
function initializeTabNavigation() {
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');

    tabButtons.forEach(button => {
        button.addEventListener('click', function() {
            const tabId = this.getAttribute('data-tab');

            // Remove active class from all buttons and contents
            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabContents.forEach(content => content.classList.remove('active'));

            // Add active class to clicked button and corresponding content
            this.classList.add('active');
            document.getElementById(tabId).classList.add('active');
        });
    });
}

/**
 * Initialize slider inputs with real-time value updates
 */
function initializeSliders() {
    const sliders = document.querySelectorAll('.slider');

    sliders.forEach(slider => {
        slider.addEventListener('input', function() {
            const valueDisplay = this.closest('.setting-control').querySelector('.value-display span:first-child');
            valueDisplay.textContent = this.value;
        });
    });
}

/**
 * Load settings from localStorage and populate UI
 */
function loadSettings() {
    try {
        const storedSettings = localStorage.getItem(SETTINGS_STORAGE_KEY);
        const settings = storedSettings ? JSON.parse(storedSettings) : DEFAULT_SETTINGS;

        // Port Scanner Settings
        updateSliderAndValue('port-threads-default', settings.portScanner.threadsDefault);
        updateSliderAndValue('port-threads-extended', settings.portScanner.threadsExtended);

        // Subdomain Finder Settings
        updateSliderAndValue('subdomain-threads-normal', settings.subdomainFinder.threadsNormal);
        updateSliderAndValue('subdomain-threads-deep', settings.subdomainFinder.threadsDeep);

        // Directory Finder Settings
        updateSliderAndValue('directory-threads-normal', settings.directoryFinder.threadsNormal);
        updateSliderAndValue('directory-threads-deep', settings.directoryFinder.threadsDeep);

        // Database Scanner Settings
        updateSliderAndValue('database-threads', settings.databaseScanner.threads);

        showStatus('Settings loaded successfully', 'success', 2000);
    } catch (error) {
        console.error('Error loading settings:', error);
        showStatus('Error loading settings. Using defaults.', 'error', 3000);
        // Reset to defaults if there's an error
        resetToDefaults();
    }
}

/**
 * Save settings to localStorage
 */
function saveSettings() {
    try {
        const settings = {
            portScanner: {
                threadsDefault: parseInt(document.getElementById('port-threads-default').value),
                threadsExtended: parseInt(document.getElementById('port-threads-extended').value)
            },
            subdomainFinder: {
                threadsNormal: parseInt(document.getElementById('subdomain-threads-normal').value),
                threadsDeep: parseInt(document.getElementById('subdomain-threads-deep').value)
            },
            directoryFinder: {
                threadsNormal: parseInt(document.getElementById('directory-threads-normal').value),
                threadsDeep: parseInt(document.getElementById('directory-threads-deep').value)
            },
            databaseScanner: {
                threads: parseInt(document.getElementById('database-threads').value)
            }
        };

        // Validate settings
        if (!validateSettings(settings)) {
            showStatus('Invalid settings. Please check your values.', 'error', 3000);
            return;
        }

        localStorage.setItem(SETTINGS_STORAGE_KEY, JSON.stringify(settings));
        
        // Send settings to server for session storage
        sendSettingsToServer(settings);
        
        showStatus('✓ Settings saved successfully', 'success', 3000);
    } catch (error) {
        console.error('Error saving settings:', error);
        showStatus('Error saving settings. Please try again.', 'error', 3000);
    }
}

/**
 * Send settings to server for session storage
 */
function sendSettingsToServer(settings) {
    fetch('/api/save-settings', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(settings)
    })
    .catch(error => {
        console.error('Error sending settings to server:', error);
        // Settings are saved locally, so this is not critical
    });
}

/**
 * Reset all settings to defaults
 */
function resetToDefaults() {
    if (confirm('Are you sure you want to reset all settings to default values?')) {
        // Port Scanner Settings
        updateSliderAndValue('port-threads-default', DEFAULT_SETTINGS.portScanner.threadsDefault);
        updateSliderAndValue('port-threads-extended', DEFAULT_SETTINGS.portScanner.threadsExtended);

        // Subdomain Finder Settings
        updateSliderAndValue('subdomain-threads-normal', DEFAULT_SETTINGS.subdomainFinder.threadsNormal);
        updateSliderAndValue('subdomain-threads-deep', DEFAULT_SETTINGS.subdomainFinder.threadsDeep);

        // Directory Finder Settings
        updateSliderAndValue('directory-threads-normal', DEFAULT_SETTINGS.directoryFinder.threadsNormal);
        updateSliderAndValue('directory-threads-deep', DEFAULT_SETTINGS.directoryFinder.threadsDeep);

        // Database Scanner Settings
        updateSliderAndValue('database-threads', DEFAULT_SETTINGS.databaseScanner.threads);

        // Auto-save the default settings
        saveSettings();
    }
}

/**
 * Update slider value and display
 */
function updateSliderAndValue(elementId, value) {
    const slider = document.getElementById(elementId);
    const valueDisplay = slider.closest('.setting-control').querySelector('.value-display span:first-child');
    
    slider.value = value;
    valueDisplay.textContent = value;
}

/**
 * Validate settings
 */
function validateSettings(settings) {
    // Port Scanner
    if (settings.portScanner.threadsDefault < 1 || settings.portScanner.threadsDefault > 500) return false;
    if (settings.portScanner.threadsExtended < 1 || settings.portScanner.threadsExtended > 500) return false;

    // Subdomain Finder
    if (settings.subdomainFinder.threadsNormal < 1 || settings.subdomainFinder.threadsNormal > 800) return false;
    if (settings.subdomainFinder.threadsDeep < 1 || settings.subdomainFinder.threadsDeep > 800) return false;

    // Directory Finder
    if (settings.directoryFinder.threadsNormal < 1 || settings.directoryFinder.threadsNormal > 1000) return false;
    if (settings.directoryFinder.threadsDeep < 1 || settings.directoryFinder.threadsDeep > 1000) return false;

    // Database Scanner
    if (settings.databaseScanner.threads < 1 || settings.databaseScanner.threads > 50) return false;

    return true;
}

/**
 * Show status message
 */
function showStatus(message, type = 'success', duration = 3000) {
    const statusEl = document.getElementById('statusMessage');
    statusEl.textContent = message;
    statusEl.className = `status-message show ${type}`;

    if (duration > 0) {
        setTimeout(() => {
            statusEl.classList.remove('show');
        }, duration);
    }
}

/**
 * Get scanner settings
 */
function getScannerSettings(scannerType) {
    try {
        const storedSettings = localStorage.getItem(SETTINGS_STORAGE_KEY);
        const settings = storedSettings ? JSON.parse(storedSettings) : DEFAULT_SETTINGS;

        switch(scannerType) {
            case 'port':
                return settings.portScanner;
            case 'subdomain':
                return settings.subdomainFinder;
            case 'directory':
                return settings.directoryFinder;
            case 'database':
                return settings.databaseScanner;
            default:
                return null;
        }
    } catch (error) {
        console.error('Error getting scanner settings:', error);
        return null;
    }
}

/**
 * Get thread count for specific scanner and mode
 * @param {string} scannerType - 'port', 'subdomain', 'directory', 'database'
 * @param {string} mode - 'default', 'extended', 'normal', 'deep', etc.
 */
function getThreadCount(scannerType, mode = 'default') {
    const settings = getScannerSettings(scannerType);
    if (!settings) return null;

    const modeKey = mode.charAt(0).toUpperCase() + mode.slice(1).toLowerCase();
    
    // For single-value settings like database
    if (settings.threads !== undefined) {
        return settings.threads;
    }

    // For multi-value settings
    const key = `threads${modeKey}`;
    return settings[key] || null;
}

/**
 * Check if user has custom settings
 */
function hasCustomSettings() {
    try {
        const storedSettings = localStorage.getItem(SETTINGS_STORAGE_KEY);
        return storedSettings !== null;
    } catch (error) {
        return false;
    }
}

// Export functions for use in other scripts
window.scannerSettings = {
    loadSettings,
    saveSettings,
    resetToDefaults,
    getScannerSettings,
    getThreadCount,
    hasCustomSettings,
    DEFAULT_SETTINGS
};
