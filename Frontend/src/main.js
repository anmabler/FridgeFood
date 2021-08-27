import { createApp } from 'vue'
import App from './App.vue'
import router from './router.js'
import store from './store.js'


let app = createApp(App)
app.use(router)
app.use(store)
app.mount('#app')
// createApp(App).mount('#app')
