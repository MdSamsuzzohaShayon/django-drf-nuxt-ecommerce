// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: {
    enabled: true,
    vscode: {},
  },
  typescript: {
    strict: true
  },
  modules: [
    '@pinia/nuxt',
    '@nuxtjs/tailwindcss',
    'nuxt-icon',
    '@nuxt/devtools',
  ],
  app: {
    head: {
      title: "Shakil Furniture",
      meta: [
        { name: 'description', content: 'A furniture website' }
      ],
      link: [
        { rel: 'stylesheet', href: 'https://fonts.googleapis.com/icon?family=Material+Icons' }
      ],
      charset: 'utf-8',
      viewport: 'width=device-width, initial-scale=1',
    }
  },
  components: [
    { path: '~/components/product', extensions: ['vue']},
    { path: '~/components/category', extensions: ['vue']},
    { path: '~/components/order', extensions: ['vue']},
    { path: '~/components/setting', extensions: ['vue']},
    { path: '~/components/user', extensions: ['vue']},
    '~/components'
  ]
})
