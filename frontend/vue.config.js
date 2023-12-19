const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: [
    'quasar'
  ],

  assetsDir: 'static',
  publicPath: process.env.NODE_ENV === 'production'
    ? '/pptx-maker/'
    : '/',

  pluginOptions: {
    quasar: {
      importStrategy: 'kebab',
      rtlSupport: false
    }
  }
})
