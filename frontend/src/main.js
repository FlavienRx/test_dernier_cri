import Vue from "vue";
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import * as Sentry from "@sentry/vue";
import { Integrations } from "@sentry/tracing";

Sentry.init({
    Vue: Vue,
    dsn: "https://f0bf91902d4a47c7b18660310b8c513d@o481806.ingest.sentry.io/5851254",
    integrations: [new Integrations.BrowserTracing()],

    // We recommend adjusting this value in production, or using tracesSampler
    // for finer control
    tracesSampleRate: 1.0,
});

// Create pokemon app
const app = createApp(App)

// Add router to pokemon app
app.use(router)

// Mount pokemon app
app.mount('#app')