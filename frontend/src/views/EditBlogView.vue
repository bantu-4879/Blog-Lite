<script setup lang="ts">
import axios from 'axios';
</script>

<template>
    <div class="login-box">
  <h2>Edit Blog</h2>
  <form>
    <div class="user-box">
      <input v-model="title" type="text" id="title" required= true :placeholder="`${title}`">
      <label>Title</label>
    </div>
    <div class="user-box">
      <input v-model="caption" type="text" id="caption" required= true :placeholder="`${caption}`">
      <label>Caption</label>
    </div>
    <div class="user-box">
      <input v-model="image_url" type="text" id="image_url" required= true :placeholder="`${image_url}`">
      <label>Image URL</label>
    </div>
    <a @click.prevent="submitForm">
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      Submit
    </a>
  </form>
</div>
</template>


<script lang="ts">
  
  export default {
    props: {
        blog_id: {
            type: String,
            required: true,
        },
    },
    
    data() {
      return {
        title: "",
        caption: "",
        image_url: "",
        content: "",
      };
    },
    mounted() {
      fetch(`http://127.0.0.1:5000/page/${this.blog_id}`)
      .then(response => response.json())
      .then(data => {
        this.title = data["blog_title"]
        this.caption = data["blog_caption"]
        this.image_url = data["blog_image_url"]
        

    })

    },

    methods:{
      submitForm() {
        const putdata = {
          title: this.title,
          caption: this.caption,
          image_url: this.image_url,
        };
        axios.put(`http://127.0.0.1:5000/deleteblog/${this.blog_id}`, putdata)
        .then(this.$router.push({ name: 'theblog' ,params: { id : this.blog_id}}))
      }
      

    }
    
  };
</script>

<style>
html {
  height: 100%;
}
body {
  margin:0;
  padding:0;
  font-family: sans-serif;
  
}

.login-box {
  margin-top:80px;
  position: absolute;
  top: 50%;
  left: 50%;
  width: 60%;
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

</style>
