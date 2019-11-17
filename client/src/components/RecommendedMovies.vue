<template>
  <div class="row align-items-center justify-content-center bg-dark">
    <div class="container">
      <div class="ff-header">
        <h1>RECOMMENDED FOR YOU</h1>
        <h2>Similar movies you might like →</h2>
      </div>
    </div>
    <div class="row align-items-center justify-content-center ">
      <movie-thumbnail
        v-for="(n,i) in suggested_movies"
        :key="i.id"
        :name="n.name"
        :year="n.year"
        :poster="n.poster"
      ></movie-thumbnail>
    </div>
  </div>
</template>

<script>
import MovieThumbnail from './MovieThumbnail.vue';

export default {
  name: 'RecommendedMovies',
  components: { MovieThumbnail },
  props: ['suggested_movies'],
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
