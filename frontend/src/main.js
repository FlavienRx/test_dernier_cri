import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// Create pokemon app
const app = createApp(App)

// Add router to pokemon app
app.use(router)

// Mount pokemon app
app.mount('#app')