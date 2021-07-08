<template>
  <div class="detail">
    <div class="title">
      <div class="column">
        <h1>{{ pokemon.name }}</h1>
      </div>
      <div class="column">
        <h3>HP {{ hp }}</h3>
      </div>
    </div>
    <div class="image">
      <img :src="pokemon.large_image_url" />
    </div>
    <div class="description">
      <div class="column">
        <p>Types:</p>
        <li v-for="type in pokemon.types" :key="type.id">
          {{ type.name }}
        </li>
      </div>
      <div class="column">
        <p>Moves</p>
        <li v-for="move in pokemon.moves" :key="move.id">
          {{ move.name }}
        </li>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "PokemonDetail",
  props: ["id"],
  data() {
    return {
      pokemon: {}, // Array for holding the pokemon infos
      hp: Number, // Number holding pokemon HP
    };
  },
  mounted() {
    // This will fetch pokemon when PokemonDetail is loaded
    this.getPokemon();
    this.getHp();
  },
  methods: {
    getPokemon() {
      axios({
        method: "get",
        url: "/api/pokemon/" + this.id,
      }).then((response) => (this.pokemon = response.data));
    },
    getHp() {
      this.hp = Math.floor(Math.random() * 100); //multiply to generate random number between 0, 100
    },
  },
};
</script>

<style scoped>
.detail {
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
  background-color: lightgray;
  border: 15px solid yellow;
  border-radius: 15px;
  margin-left: 30%;
  margin-right: 30%;
  padding-bottom: 15px;
}
.title {
  display: flex;
  justify-content: space-between;
  text-align: left;
  margin-left: 20px;
}
.image {
  border: 5px solid gray;
  margin-left: 15px;
  margin-right: 15px;
  background-color: white;
}
.description {
  display: flex;
  justify-content: center;
  text-align: left;
}
.column {
  margin-left: 20px;
  margin-right: 20px;
}
</style>