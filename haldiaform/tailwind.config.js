// @type {import('tailwindcss').Config}
module.exports = {
  content: [
      './form/templates/**/*.html',
      './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {},
  },
  plugins: [require('flowbite/plugin')],
  darkMode: 'media',
}

