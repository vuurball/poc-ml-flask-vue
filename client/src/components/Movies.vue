<template>
  <div>
    <div class="row align-items-center justify-content-center bg-light">
      <div class="container">
        <p style="text-align: center;">
          <span class="text-highlight">
            <strong>
              <span style="font-size: 12px;">* * *&nbsp;<span style="font-size: 16px;">☞</span>
              &nbsp;
              <span style="font-family: Montserrat;">TRANDING MOVIES</span>
              &nbsp;
              <span style="font-size: 16px;">☜</span>
              &nbsp;* * *
              </span>
            </strong>
          </span>
        </p>
        <div style="margin:10px 100px;">
          <span v-for="(n,i) in movies" :key="i.id" @click="suggestions(i)">
            <span class="pill" :class="[i == active_movie ? 'is-selected' : '']">
              {{n}}
            </span>
          </span>
        </div>
      </div>
    </div>
    <div class="row align-items-center justify-content-center bg-dark">
      <div class="container">
        <div class="ff-header">
          <h1>RECOMMENDED FOR YOU</h1>
          <h2>Similar movies you might like →</h2>
        </div>
      </div>
      <div class="row align-items-center justify-content-center ">
        <div class="card" style="width: 18rem;" v-for="(n,i) in suggested_movies" :key="i.id">
          <img :src=n.poster class="card-img-top" alt="#">
          <div class="card-body">
            <h5 class="card-title">{{ n.name }} ({{ n.year }})</h5>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Movisuggested_movieses',
  data() {
    return {
      movies: '',
      active_movie: 0,
      suggested_movies: '',
      api: '',
    };
  },
  methods: {
    getMovies() {
      const path = 'http://127.0.0.1:5000/movies';
      axios.get(path)
        .then((res) => {
          this.movies = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    suggestions(id) {
      this.active_movie = id;
      this.getSuggestionByMovie();
    },
    getSuggestionByMovie() {
      const path = `http://127.0.0.1:5000/movies/${this.active_movie}`;
      axios.get(path)
        .then((res) => {
          // for (let i = 0; i < res.data.length(); i += 1) {
          this.suggested_movies = res.data;
          this.getMovieData();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    getMovieData() {
      const data = this.suggested_movies;
      const keys = Object.keys(data);
      const values = Object.values(data);
      const fullMoviesData = [];
      for (let i = 0; i <= keys.length; i += 1) {
        if (Object.prototype.hasOwnProperty.call(values, i)) {
          axios.get(`http://www.omdbapi.com/?apikey=6362656e&s=${values[i].name}`)
            .then((success) => {
              const arr = success.data.Search;
              let row = [];
              let row1 = [];
              let url = '#';
              let date = 'Unknown';
              [row, row1, row1, row1, row1] = arr;
              if (row.Poster === 'N/A') {
                url = 'https://static-vectorplace-com.ams3.digitaloceanspaces.com/uploads/works/72680/preview_72680.jpg';
              } else {
                url = row.Poster;
              }
              date = row.Year;
              row = row1;
              fullMoviesData.push({
                name: values[i].name,
                poster: url,
                year: date,
              });
            });
        }
      }
      this.suggested_movies = fullMoviesData;
    },
  },
  created() {
    this.getMovies();
    this.getSuggestionByMovie();
  },
};
</script>
