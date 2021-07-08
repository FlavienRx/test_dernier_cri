import { createRouter, createWebHistory } from 'vue-router'
import PokemonList from '@/components/PokemonList'
import PokemonDetail from '@/components/PokemonDetail'

const routes = [
    {
        path: '/',
        name: 'List',
        component: PokemonList
    },
    {
        path: '/detail/:id',
        name: 'Detail',
        component: PokemonDetail,
        props: true
    }
]
const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})
export default router