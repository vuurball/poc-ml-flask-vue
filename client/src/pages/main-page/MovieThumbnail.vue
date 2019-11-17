<template>
  <div class="card" style="width: 18rem;">
    <img :src=moviePoster class="card-img-top" alt="#">
    <div class="card-body">
      <h5 class="card-title">{{ movieName }} ({{ movieYear }})</h5>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieThumbnail',
  props: ['movieName', 'movieYear', 'moviePoster'],
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

  .card{
    color: white;
    margin: 10px;
    background-color:rgb(92, 15, 78);
  }

  .card h5 {
    color:#9a5e9a;
  }
  .img-thumbnail {
    max-width: 100px;
  }
</style>
