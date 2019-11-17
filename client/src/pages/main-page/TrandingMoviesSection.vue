<template>
  <div class="row align-items-center justify-content-center bg-light">
    <div class="mx-4">
      <p style="text-align: center;">
        <span class="text-highlight">
          <strong>
            <span style="font-size: 22px;">
              <span style="font-size: 16px;" class="mr-2">* * * ☞</span>
              <span style="font-family: Montserrat;">
                TRANDING MOVIES
              </span>
              <span style="font-size: 16px;" class="mr-2">☜ * * *</span>
            </span>
          </strong>
        </span>
      </p>
      <div class="row align-items-center justify-content-center ">
        <movie-thumbnail
          v-for="(n,i) in movies"
          :key="i"
          :movieName="n.name"
          :movieYear="n.year"
          :moviePoster="n.poster"
          :movieId="i"
          class="trending-section"
          :class="[i == active_movie ? 'is-selected' : '']"
          :showTitle=false
          ></movie-thumbnail>

      </div>
    </div>
  </div>
</template>

<script>
import MovieThumbnail from './MovieThumbnail.vue';

export default {
  name: 'TrandingMoviesSection',
  components: { MovieThumbnail },
  props: ['movies', 'active_movie'],
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .text-highlight {
    text-align: center;
    background-image: url('https://social-streams.com/wp-content/themes/Total/assets/images/highlight-left.png'),
    url('https://social-streams.com/wp-content/themes/Total/assets/images/highlight-center.png'),
    url('https://social-streams.com/wp-content/themes/Total/assets/images/highlight-right.png');
    background-repeat: repeat-x;
    background-repeat: no-repeat, repeat-x, no-repeat;
    background-position: center;
    background-position: left, center, right;
    background-clip: padding-box, content-box, padding-box;
    color: #a5651a;
    padding: 0 20px;
    margin: 0 -6px;
  }
</style>
