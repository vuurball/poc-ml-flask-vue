<template>
  <div class="row align-items-center justify-content-center bg-light">
    <div class="container">
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
      <div style="margin:10px 100px;">
        <span v-for="(name,i) in movies" :key="i.id" @click="$emit('movie-selected', i)">
          <span class="pill" :class="[i == active_movie ? 'is-selected' : '']">
            {{name}}
          </span>
        </span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TrandingMovies',
  props: ['movies', 'active_movie'],
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .pill {
    border: 1px solid #ddd;
    border-color: #9a5e9a;
    font-size: 16px;
    font-weight: 400;
    color: #9A5E9A;
    vertical-align: baseline;
    cursor: pointer;
    margin-right: 12px;
    margin-bottom: 12px;
    float: none;
    display: inline-block;
    margin: 0 5px 5px 0;
    padding: .2em 1em;
    font-family: "Montserrat";
    box-sizing: border-box;
    text-align: center;
    border-radius: 0;
  }

  .is-selected {
    background: #9a5e9a;
    color: #fff;
  }
</style>
