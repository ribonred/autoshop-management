module.exports = { 
  mode: 'jit',
  content: [ 
      './templates/**/*.html',
      './**/**/*.html'

  ], 
  theme: { 
    extend: {}, 
  }, 
  plugins: [
    require('@tailwindcss/forms'),
  ], 
}