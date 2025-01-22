import { defineConfig } from 'eslint-define-config';
import react from 'eslint-plugin-react';

export default defineConfig({
    languageOptions: {
        globals: {
            browser: true,
            es2021: true,
        },
        parserOptions: {
            ecmaFeatures: {
                jsx: true,
            },
            ecmaVersion: 12,
            sourceType: 'module',
        },
    },
    plugins: {
        react: react,
    },
    rules: {
        // Add custom rules here
        'no-unused-vars': 'warn',
        'react/prop-types': 'off',
    },
});
