import { createApp } from 'vue'
import App from './App.vue'
import router from './router.js'


let app = createApp(App)
app.use(router)
app.mount('#app')
// createApp(App).mount('#app')
