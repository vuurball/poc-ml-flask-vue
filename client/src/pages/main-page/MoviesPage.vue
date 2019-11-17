<template>
  <div>
    <!-- first section -->
    <tranding-movies-section
      :movies=movies
      :active_movie=active_movie
      v-on:movie-selected="selectActiveMovie($event)"
    ></tranding-movies-section>
    <!-- second section -->
    <recommended-movies-section
      :suggested_movies=suggested_movies
    ></recommended-movies-section>
  </div>
</template>

<script>
import axios from 'axios';
import TrandingMoviesSection from './TrandingMoviesSection.vue';
import RecommendedMoviesSection from './RecommendedMoviesSection.vue';

export default {
  name: 'Movies',
  components: { TrandingMoviesSection, RecommendedMoviesSection },
  data() {
    return {
      movies: '',
      active_movie: 0,
      suggested_movies: '',
    };
  },
  methods: {
    getTrandingMovies() {
      const path = 'http://127.0.0.1:5000/movies';
      axios.get(path)
        .then((res) => {
          this.movies = res.data;
          this.getTradingMovieData();
          this.getSuggestionByMovie();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    /**
     * $event = movie id
     */
    selectActiveMovie($event) {
      this.active_movie = $event;
      this.getSuggestionByMovie();
    },
    /**
     * call backend api to get a list of suggested movies
     * based on the this.active_move
     */
    getSuggestionByMovie() {
      const path = `http://127.0.0.1:5000/movies/${this.active_movie}`;
      axios.get(path)
        .then((res) => {
          this.suggested_movies = res.data;
          this.getMovieData();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    /**
     * call external api to get movie info a poster url by name
     */
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
    getTradingMovieData() {
      const data = this.movies;
      const values = Object.values(data);
      const fullMoviesData = [];
      for (let i = 0; i <= values.length; i += 1) {
        if (Object.prototype.hasOwnProperty.call(values, i)) {
          axios.get(`http://www.omdbapi.com/?apikey=6362656e&s=${values[i]}`)
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
                name: values[i],
                poster: url,
                year: date,
                id: i,
              });
            });
        }
      }
      this.movies = fullMoviesData;
    },
  },
  created() {
    this.getTrandingMovies();
  },
};
</script>
