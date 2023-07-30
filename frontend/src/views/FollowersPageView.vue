<script setup lang="ts">
import axios from 'axios';
</script>

<template>
    <div class="wrap">

  <div v-for="i in follow">
  <div class="box">
    <div class="box-top">
      <img class="box-image" src="https://images.unsplash.com/photo-1564594736624-def7a10ab047?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8MXx8fGVufDB8fHx8&w=1000&q=80" alt="Girl Eating Pizza">
      <div class="title-flex">
        <h3 class="box-title">{{ i[1] }}</h3>
        
      </div>
      <p class="description">{{ i[2] }}</p>
    </div>
    <div class="log">
    <a @click="unfollow(i[0])" class="login-box">
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      UnFollow {{ i[1] }}
    </a>
    </div>
  </div>
</div>
  
<div v-for="i in notfollow">
  <div class="box">
    <div class="box-top">
      <img class="box-image" src="https://res.cloudinary.com/du5jifpgg/image/upload/t_opengraph_image/Parcours/itin%C3%A9raires/Disneyland-et-alentours/Fetes-de-fin-d-annee-2021-a-disneyland-paris-header.jpg" alt="Girl Eating Pizza">
      <div class="title-flex">
        <h3 class="box-title">{{ i[1] }}</h3>
        
      </div>
      <p class="description">{{ i[2] }}</p>
    </div>
    <div class="log">
    <a @click="newfollow(i[0])" class="login-box">
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      Follow {{ i[1] }}
    </a>
    </div>
  </div>
</div>
  
  
</div>
</template>


<script lang="ts">

export default{
  props: {
    author: {
      type: String,
      required: true,
    }, 
    
  },

  data(){
    return {
      follow: [],
      notfollow: [],
      

    }
  },

  mounted() {
    this.fetchData();
  },


  methods:{

    fetchData() {
      axios.get(`http://127.0.0.1:5000/followerpagedata/${this.author}`)
        .then(response => {
          this.notfollow = response.data["can_follow"];
          this.follow = response.data["already_follow"];
        })
    },

    unfollow(follower_id: number) {
      axios.delete(`http://127.0.0.1:5000/followerpagedata/${this.author}/${follower_id}`)
      .then(() => {
          this.fetchData();
       })
    },

    newfollow(follower_id: number) {
        const postdata = {
            user : this.author,
            follower_id : follower_id

        };
        axios.post(`http://127.0.0.1:5000/followerpagedata`, postdata)
        .then(() => {
          this.fetchData();
       })
    }  
    
  }

}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Antic+Didone&display=swap');

* {
  box-sizing: border-box;
  padding: 0;
  margin: 0;
}

:root {
  --purple: hsl(240, 80%, 89%);
  --pink: hsl(0, 59%, 94%);
  --light-bg: hsl(204, 37%, 92%);
  --light-gray-bg: hsl(0, 0%, 94%);
  --white: hsl(0, 0%, 100%);
  --dark: hsl(0, 0%, 7%);
  --text-gray: hsl(0, 0%, 30%);
}

body {
  background: var(--light-bg);
  font-family: 'Antic Didone', serif;
  color: var(--dark);
}

h3 {
  font-size: 1.5em;
  font-weight: 700;
}

p {
  font-size: 1em;
  line-height: 1.7;
  font-weight: 300;
  color: var(--text-gray);
}

.description {
  white-space: wrap;
}

a {
  text-decoration: none;
  color: inherit;
}

.wrap {
  display: flex;
  justify-content: space-between;
  align-items: stretch;
  width: 100%;
  gap: 24px;
  padding: 24px;
  flex-wrap: wrap;
}

.box {
  display: flex;
  flex-direction: column;
  flex-basis: 100%;
  position: relative;
  padding: 24px;
  background: #fff;
  width: 320px;
  height: 600px;
}

.box-top {
  display: flex;
  flex-direction: column;
  position: relative;
  gap: 12px;
  margin-bottom: 10px;
}

.box-image {
  width: 100%;
  height: 360px;
  object-fit: cover;
  object-position: 50% 20%;
}

.title-flex {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.box-title {
  border-left: 3px solid var(--purple);
  padding-left: 12px;
}

.user-follow-info {
  color: hsl(0, 0%, 60%);
}

.button {
  display: block;
  justify-content: center;
  align-items: center;
  text-align: center;
  margin-top: auto;
  padding: 16px;
  color: #000;
  background: transparent;
  box-shadow: 0px 0px 0px 1px black inset;
  transition: background 0.4s ease;
}

.button:hover {
  background: var(--purple);
}

.fill-one {
  background: var(--light-bg);
}

.fill-two {
  background: var(--pink);
}
.log {
  cursor: pointer;
}

.log a {
  width: 100%;
  position: relative;
  display: inline-block;
  padding: 10px 20px;
  color: #03e9f4;
  font-size: 16px;
  font-weight: bolder;
  text-decoration: none;
  text-transform: uppercase;
  overflow: hidden;
  transition: .5s;
  margin-top: 25px;
  letter-spacing: 4px;
  
  
}

.log a:hover {
  background: #03e9f4;
  color: #fff;
  border-radius: 5px;
  box-shadow: 0 0 5px #03e9f4,
              0 0 25px #03e9f4,
              0 0 50px #03e9f4,
              0 0 100px #03e9f4;
}

.log a span {
  position: absolute;
  display: block;
}

.log a span:nth-child(1) {
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

.log a span:nth-child(2) {
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

.log a span:nth-child(3) {
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

.log a span:nth-child(4) {
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

/* RESPONSIVE QUERIES */

@media (min-width: 320px) {
  .title-flex {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: start;
  }
  .user-follow-info {
    margin-top: 6px;
  }
}

@media (min-width: 460px) {
  .title-flex {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: start;
  }
  .user-follow-info {
    margin-top: 6px;
  }
}

@media (min-width: 640px) {
  .box {
    flex-basis: calc(50% - 12px);
  }
  .title-flex {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: start;
  }
  .user-follow-info {
    margin-top: 6px;
  }
}

@media (min-width: 840px) {
  .title-flex {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: start;
  }
  .user-follow-info {
    margin-top: 6px;
  }
}

@media (min-width: 1024px) {
  .box {
    flex-basis: calc(33.3% - 16px);
  }
  .title-flex {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: start;
  }
  .user-follow-info {
    margin-top: 6px;
  }
}

@media (min-width: 1100px) {
  .box {
    flex-basis: calc(25% - 18px);
  }
}

</style>