<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import axios from 'axios';
</script>

<template>

    <header v-if="verified">
      <div class="heading">
        <div class="heading-text">Feed</div>
      </div>
        
      <nav>
          <RouterLink :to="{ name: 'home', params: { author: id } }">Home</RouterLink>
          <RouterLink :to="{ name: 'profile', params: { name: username} }">Profile</RouterLink>
          <RouterLink :to="{ name: 'newblog', params: { author : id} }">New Blog</RouterLink>
          <RouterLink :to="{ name: 'myblog', params: { author: id } }">My Blogs</RouterLink>
          <RouterLink :to="{ name: 'search', params: { user: id } }">Search</RouterLink>
          <RouterLink :to="{ name: 'report', params: { author: id }}">Export Data</RouterLink>
          <RouterLink :to="{ name: 'follower', params: { author: id }}">Followers</RouterLink>
        </nav>
    </header>

  <div class="login-box" v-if="!verified">
    <h2>Enter the Credentials</h2>
    <form>
      <div class="user-box">
        <input v-model="username" type="text" id="username" required= true>
        <label>Username</label>
      </div>
      <div class="user-box">
        <input v-model="password" type="password" id="password" required= true>
        <label>Password</label>
      </div>
      <div class="inputclick">
      <a @click="verify">
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        Login
      </a>

      <a @click="signup">
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        Sign In
      </a>
      </div>

    </form>
  </div>

  
  <RouterView :author="id" v-if="verified"/>
   
</template>


<script lang="ts">
export default{
  data() {
      return {
        id: 0,
        username: "",
        password: "",
        verified: false,
        fetchedpass: "",
      };
  },
  methods:{
    verify(){
      fetch(`http://127.0.0.1:5000/login/${this.username}`)
      .then(response => response.json())
      .then(data => {
          if( this.password == data["password"]){
             this.id = data["user_id"]
             this.verified = true
          }
      })
    },
    signup(){
      const postdata = {
          username: this.username,
          password: this.password,
      };
      axios.post('http://127.0.0.1:5000/login/new', postdata);

      const otherpostdata = {
        user_name : this.username,

      };
      axios.post('http://127.0.0.1:5000/user/new', otherpostdata)
      
      
    }   
  },
  mounted() {
    const parameter = this.username;
    fetch(`http://127.0.0.1:5000/login/${parameter}`)
    .then(response => response.json())
    .then(data => {
      this.id = data["user_id"]
    })
  },

}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Antic+Didone&display=swap');


header{
  display:block;
  width:100%;
  height: 100%;
}

.heading{
  width: 100%;
  height: 112px;
}

.heading .heading-text {
  text-align: center;
  font-family: 'Antic Didone', serif;
  font-size: 3em;
  padding-top: 30px;

}

nav {
  width: 100%;
  font-size: 18px;
  letter-spacing: 2px;
  text-align: center;
  margin-top: -1rem;
  font-family: 'Antic Didone', serif;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
nav {
    text-align: center;
    font-size: 18px;
    letter-spacing: 2px;
    padding: 1rem 0;
    margin-top: -1rem;
  }
}

html {
  height: 100%;
}
body {
  margin:0;
  padding:0;
  font-family: sans-serif;
  
}

.login-box {
  margin-top:30px;
  position: absolute;
  cursor: pointer;
  top: 50%;
  left: 50%;
  width: 45%;
  padding: 40px;
  transform: translate(-50%, -50%);
  background: linear-gradient(#141e30, #243b55);
  box-sizing: border-box;
  box-shadow: 0 15px 25px rgba(0,0,0,.6);
  border-radius: 10px;
}

.login-box h2 {
  margin: 0 0 30px;
  padding: 0;
  color: #fff;
  text-align: center;
  font-family: 'Antic Didone', serif;
}

.login-box .user-box {
  position: relative;
}

.login-box .user-box input {
  width: 100%;
  padding: 10px 0;
  font-size: 16px;
  color: #fff;
  margin-bottom: 30px;
  border: none;
  border-bottom: 1px solid #fff;
  outline: none;
  background: transparent;
}
.login-box .user-box label {
  position: absolute;
  top:0;
  left: 0;
  padding: 10px 0;
  font-size: 16px;
  color: #fff;
  pointer-events: none;
  transition: .5s;
}

.login-box .user-box input:focus ~ label,
.login-box .user-box input:valid ~ label {
  top: -20px;
  left: 0;
  color: #03e9f4;
  font-size: 12px;
}

.login-box form a {
  position: relative;
  display: inline-block;
  padding: 10px 20px;
  color: #03e9f4;
  font-size: 16px;
  text-decoration: none;
  text-transform: uppercase;
  overflow: hidden;
  transition: .5s;
  margin-top: 40px;
  letter-spacing: 4px
}

.login-box a:hover {
  background: #03e9f4;
  color: #fff;
  border-radius: 5px;
  box-shadow: 0 0 5px #03e9f4,
              0 0 25px #03e9f4,
              0 0 50px #03e9f4,
              0 0 100px #03e9f4;
}

.login-box a span {
  position: absolute;
  display: block;
}



.login-box a span:nth-child(1) {
  top: 0;
  left: -100%;
  width: 100%;
  height: 2px;
  background: linear-gradient(90deg, transparent, #03e9f4);
  animation: btn-anim1 1s linear infinite;
}

@keyframes btn-anim1 {
  0% {
    left: -100%;
  }
  50%,100% {
    left: 100%;
  }
}

.login-box a span:nth-child(2) {
  top: -100%;
  right: 0;
  width: 2px;
  height: 100%;
  background: linear-gradient(180deg, transparent, #03e9f4);
  animation: btn-anim2 1s linear infinite;
  animation-delay: .25s
}

@keyframes btn-anim2 {
  0% {
    top: -100%;
  }
  50%,100% {
    top: 100%;
  }
}

.login-box a span:nth-child(3) {
  bottom: 0;
  right: -100%;
  width: 100%;
  height: 2px;
  background: linear-gradient(270deg, transparent, #03e9f4);
  animation: btn-anim3 1s linear infinite;
  animation-delay: .5s
}

@keyframes btn-anim3 {
  0% {
    right: -100%;
  }
  50%,100% {
    right: 100%;
  }
}

.login-box a span:nth-child(4) {
  bottom: -100%;
  left: 0;
  width: 2px;
  height: 100%;
  background: linear-gradient(360deg, transparent, #03e9f4);
  animation: btn-anim4 1s linear infinite;
  animation-delay: .75s
}

@keyframes btn-anim4 {
  0% {
    bottom: -100%;
  }
  50%,100% {
    bottom: 100%;
  }
}

.inputclick{
width: 100%;
display: flex;
justify-content: space-between;
}

</style>
