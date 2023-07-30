<script setup lang="ts">
import axios from 'axios';
</script>

<template>
    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css" rel="stylesheet">
<div class="container">

<div class="be-comment-block">
	<h1 class="comments-title">Comments</h1>

    <div v-for="i in comm_data" class="be-comment">
      <div class="be-img-comment">	
        <a href="blog-detail-2.html">
          <img src="https://bootdey.com/img/Content/avatar/avatar1.png" alt="" class="be-ava-comment">
        </a>
      </div>
      <div class="be-comment-content">
        
        <span class="be-comment-name">
          <a href="blog-detail-2.html">{{ i[2] }}</a>
        </span>
          

        <p class="be-comment-text">
          {{ i[1] }}
        </p>
      </div>
	  </div>
</div>

	  <div class="login-box">
      <h2>New Comment</h2>
      <form>
      

      <div class="user-box">
      <input v-model="comment" type="text" id="comment" required= true>
      <label>Comment</label>
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
</div>

</template>


<script lang="ts">
export default{
  props: {
    blog_id: {
      type: String,
      required: true,
    },
    author:{
      type: String,
      required: true,
    }
  },
  data(){
    return {
        name : "",
        comment: "",
        comm_data: [],
        comm_user_id: 0,



      
      

    }
  },

  mounted() {
    this.fetchData();
  },

  methods: {

    fetchData(){
      fetch(`http://127.0.0.1:5000/commentdata/${this.blog_id}`)
      .then(response => response.json())
      .then(data => {
        this.comm_data = data;
      });

    },


    submitForm(){
      fetch(`http://127.0.0.1:5000/profiledata/${this.author}`)
      .then(response => response.json())
      .then(data => {
        this.comm_user_id = data["user_id"];

        const postdata = {
        blog_id: this.blog_id,
        comment: this.comment,
        author: this.author,
        };
        console.log(postdata);
        axios.post('http://127.0.0.1:5000/commentdata', postdata)
        .then(() => {
          this.fetchData();
        })
        
      });
          

    }, 

  }

}



</script>


<style>
@import url('https://fonts.googleapis.com/css2?family=Antic+Didone&display=swap');
body{
    margin-top:20px;
    background-color:#e9ebee;
    font-family: 'Antic Didone', serif;
}

.container{
    margin-top: 60px;
}

.be-comment-block {
    margin-bottom: 50px !important;
    border: 1px solid #edeff2;
    border-radius: 2px;
    padding: 50px 70px;
    border:1px solid #ffffff;
}

.comments-title {
    font-size: 23px;
    color: #000;
    margin-bottom: 25px;
}

.be-img-comment {
    width: 60px;
    height: 60px;
    float: left;
    margin-bottom: 25px;
}

.be-ava-comment {
    width: 60px;
    height: 60px;
    border-radius: 50%;
}

.be-comment-content {
    margin-left: 80px;
    margin-bottom: 30px;
}

.be-comment-content span {
    display: inline-block;
    width: 49%;
    margin-bottom: 5px;
}

.be-comment-name {
    font-size: 13px;
    
}

.be-comment-content a {
    color: #000;
    font-size: 15px;
}

.be-comment-content span {
    display: inline-block;
    width: 49%;
    margin-bottom: 15px;
}

.be-comment-time {
    text-align: right;
}

.be-comment-time {
    font-size: 11px;
    color: #b4b7c1;
}

.be-comment-text {
    font-size: 13px;
    line-height: 18px;
    color: #7a8192;
    display: block;
    background: #f6f6f7;
    border: 1px solid #edeff2;
    padding: 15px 20px 20px 20px;
}

.form-group.fl_icon .icon {
    position: absolute;
    top: 1px;
    left: 16px;
    width: 48px;
    height: 48px;
    background: #f6f6f7;
    color: #b5b8c2;
    text-align: center;
    line-height: 50px;
    -webkit-border-top-left-radius: 2px;
    -webkit-border-bottom-left-radius: 2px;
    -moz-border-radius-topleft: 2px;
    -moz-border-radius-bottomleft: 2px;
    border-top-left-radius: 2px;
    border-bottom-left-radius: 2px;
}

.form-group .form-input {
    font-size: 13px;
    line-height: 50px;
    font-weight: 400;
    color: #b4b7c1;
    width: 100%;
    height: 50px;
    padding-left: 20px;
    padding-right: 20px;
    border: 1px solid #edeff2;
    border-radius: 3px;
}

.form-group.fl_icon .form-input {
    padding-left: 70px;
}

.form-group textarea.form-input {
    height: 150px;
}


.login-box {
  margin-top:30%;
  position: relative;
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