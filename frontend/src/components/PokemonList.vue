<template>
  <div class="home">
    <div class="grid-container">
      <div class="grid-item" v-for="pokemon in pokemons" :key="pokemon.id">
        <router-link
          :to="{ name: 'Detail', params: { id: pokemon.poke_api_id } }"
        >
          <img :src="pokemon.small_image_url" />
          <div class="text">{{ pokemon.poke_api_id }} - {{ pokemon.name }}</div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "PokemonList",
  data() {
    return {
      pokemons: [], // Array for holding the tasks
    };
  },
  mounted() {
    // This will fetch pokemons when PokemonList is loaded
    this.getPokemons();
  },
  methods: {
    getPokemons() {
      axios({
        method: "get",
        url: "/api/pokemon",
      }).then((response) => (this.pokemons = response.data));
    },
  },
};
</script>

<style scoped>
.home {
  display: flex;
  justify-content: center;
  padding-left: 20%;
  padding-right: 20%;
}
.grid-container {
  display: inline-grid;
  grid-gap: 0px;
  grid-template-columns: auto auto auto;
}
.grid-item {
  font-size: 30px;
  text-align: center;
}
.grid-item:hover {
  background-color: lightgrey;
}
a {
  text-decoration: none;
}
.text {
  color: black;
  font-size: 16px;
  padding: 16px 32px;
}
</style>