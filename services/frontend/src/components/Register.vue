<template>
    <form @submit.prevent="register">
      <input v-model="username" placeholder="Username" required />
      <input v-model="email" type="email" placeholder="Email" required />
      <input v-model="password" type="password" placeholder="Password" required />
      <button type="submit">Register</button>
    </form>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        username: '',
        email: '',
        password: ''
      };
    },
    methods: {
      async register() {
        try {
          await axios.post('/api/register', {
            username: this.username,
            email: this.email,
            password: this.password
          });
          this.$router.push('/login');
        } catch (error) {
          console.error(error.response.data.message);
        }
      }
    }
  };
  </script>
  