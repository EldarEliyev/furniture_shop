// Language configuration - 10 dil
const languages = {
    'az': {
        name: 'Azərbaycan',
        icon: '🇦🇿',
        code: 'AZ'
    },
    'en': {
        name: 'English',
        icon: '🇬🇧',
        code: 'EN'
    },
    'tr': {
        name: 'Türkçe',
        icon: '🇹🇷',
        code: 'TR'
    },
    'ru': {
        name: 'Русский',
        icon: '🇷🇺',
        code: 'RU'
    },
    'uz': {
        name: 'O\'zbek',
        icon: '🇺🇿',
        code: 'UZ'
    },
    'ar': {
        name: 'العربية',
        icon: '🇸🇦',
        code: 'AR'
    },
    'mn': {
        name: 'Монгол',
        icon: '🇲🇳',
        code: 'MN'
    },
    'tk': {
        name: 'Türkmen',
        icon: '🇹🇲',
        code: 'TK'
    },
    'fr': {
        name: 'Français',
        icon: '🇫🇷',
        code: 'FR'
    },
    'de': {
        name: 'Deutsch',
        icon: '🇩🇪',
        code: 'DE'
    }
};

document.addEventListener('DOMContentLoaded', function() {
    // Get saved language or default to Azerbaijani
    let currentLang = localStorage.getItem('selectedLanguage') || 'az';
    
    // Initialize language
    setLanguage(currentLang);
    
    // Dropdown toggle
    const dropdownBtn = document.getElementById('langDropdownBtn');
    const dropdownMenu = document.getElementById('langDropdownMenu');
    const languageDropdown = document.querySelector('.language-dropdown');
    
    if (dropdownBtn && dropdownMenu) {
        dropdownBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            languageDropdown.classList.toggle('active');
        });
        
        // Close dropdown when clicking outside
        document.addEventListener('click', function(e) {
            if (!languageDropdown.contains(e.target)) {
                languageDropdown.classList.remove('active');
            }
        });
        
        // Language option click handlers
        document.querySelectorAll('.lang-option').forEach(option => {
            option.addEventListener('click', function() {
                const lang = this.getAttribute('data-lang');
                setLanguage(lang);
                localStorage.setItem('selectedLanguage', lang);
                languageDropdown.classList.remove('active');
            });
        });
    }
    
    function setLanguage(lang) {
        const langData = languages[lang];
        if (!langData) return;
        
        // Update dropdown button
        const currentLangIcon = document.getElementById('currentLangIcon');
        const currentLangText = document.getElementById('currentLangText');
        
        if (currentLangIcon) currentLangIcon.textContent = langData.icon;
        if (currentLangText) currentLangText.textContent = langData.code;
        
        // Update active option in dropdown
        document.querySelectorAll('.lang-option').forEach(option => {
            if (option.getAttribute('data-lang') === lang) {
                option.classList.add('active');
            } else {
                option.classList.remove('active');
            }
        });
        
        // Update all elements with data attributes
        document.querySelectorAll('[data-en]').forEach(element => {
            const langAttr = `data-${lang}`;
            if (element.hasAttribute(langAttr)) {
                element.textContent = element.getAttribute(langAttr);
            }
        });
        
        // Update placeholders
        document.querySelectorAll('[data-en-placeholder]').forEach(element => {
            const langAttr = `data-${lang}-placeholder`;
            if (element.hasAttribute(langAttr)) {
                element.placeholder = element.getAttribute(langAttr);
            }
        });
        
        // Update HTML lang attribute
        document.documentElement.lang = lang;
        
        // Update page title if it has language attributes
        const titleElement = document.querySelector('title');
        if (titleElement) {
            const titleLangAttr = `data-${lang}-title`;
            if (titleElement.hasAttribute(titleLangAttr)) {
                titleElement.textContent = titleElement.getAttribute(titleLangAttr);
            }
        }
    }
    
    // Make setLanguage available globally for debugging
    window.setLanguage = setLanguage;
});
