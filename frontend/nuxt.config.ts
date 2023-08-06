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
    pageTransition: { name: 'page', mode: 'out-in' },
    head: {
      // ChatGPT: SEO friendly meta title for furniture website of Shakil Furniture
      title: "Shakil Furniture | Discover Timeless Elegance & Quality Handcrafted Furniture",
      meta: [
        { name: 'description', content: 'Experience comfort, durability, and sophistication with Shakil Furniture' },
        // ChatGPT: SEO friendly meta keywords for emerging furniture website of Shakil Furniture 
        { name: 'keywords', content: 'Handcrafted Furniture, Timeless Elegance, Quality Home Decor, Living Room Sets, Dining Tables, Bedroom Furniture, Modern Designs, Rustic Furniture, Affordable Luxury, Comfortable Sofas, Durable Furniture, Stylish Home Furnishings, Contemporary Chairs, Elegant Home Accessories, Trendy Furniture Collections, Customizable Furniture Options, Unique Wood Finishes, Premium Furniture Brands, Sustainable Furniture, Furniture Delivery & Installation' },
        { name: 'author', content: 'Shakil' },
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
