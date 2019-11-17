<template>
  <div class="card" style="width: 18rem;">
    <img :src=poster class="card-img-top" alt="#">
    <div class="card-body">
      <h5 class="card-title">{{ name }} ({{ year }})</h5>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieThumbnail',
  props: ['name', 'year', 'poster'],
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
