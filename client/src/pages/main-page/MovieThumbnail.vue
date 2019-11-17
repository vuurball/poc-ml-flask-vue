<template>
  <div class="card" @click="$parent.$emit('movie-selected', movieId)">
    <img :src=moviePoster class="card-img-top" alt="#">
    <div v-if="showTitle">
      <p class="card-title p-2">{{ movieName }} ({{ movieYear }})</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieThumbnail',
  props: ['movieName', 'movieYear', 'moviePoster', 'movieId', 'showTitle'],
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

  .card{
    color: white;
    margin: 5px;
  }

  .trending-section {
    width: 7rem;
    border: 1px solid #ddd;
    border-color: #9a5e9a;
    font-size: 14px;
    /* font-weight: 400; */
    color: #9A5E9A;
    vertical-align: baseline;
    cursor: pointer;
    float: none;
    display: inline-block;
    margin: 12px 5px 12px 0;
    padding: 5px;
    font-family: "Montserrat";
    box-sizing: border-box;
    border-radius: 0;
  }
  .recommended-section {
    width: 12rem;
    color:#9a5e9a;
    background-color:rgb(92, 15, 78);
  }

  .is-selected {
    background: #9a5e9a;
    color: #fff;
  }
</style>
