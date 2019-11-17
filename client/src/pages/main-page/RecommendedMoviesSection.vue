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
        :movieName="n.name"
        :movieYear="n.year"
        :moviePoster="n.poster"
        class="recommended-section"
        :showTitle=true
      ></movie-thumbnail>
    </div>
  </div>
</template>

<script>
import MovieThumbnail from './MovieThumbnail.vue';

export default {
  name: 'RecommendedMoviesSection',
  components: { MovieThumbnail },
  props: ['suggested_movies'],
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.ff-header h1 {
    color: rgb(255, 255, 255);
    font-size: 44px;
    text-align: center;
    font-weight: normal;
    margin: 20px 20px 12px !important;
}

.ff-header h2 {
    color: rgb(255, 255, 255);
    font-size: 26px;
    text-align: center;
    font-weight: 300;
    margin: 12px 20px 20px !important;
    font-weight: 600;
}
</style>
