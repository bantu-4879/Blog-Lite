<script setup lang="ts">
import axios from 'axios';
</script>

<template>

  <div class="header" :style ="{ background: url}" style = "background-size: cover;">
  
  <div class="info">
    <h1>{{ title }}</h1>
    <div class="meta">
      <a  href="https://twitter.com/nodws" target="_b" class="author"></a><br>
      By <a href="https://twitter.com/nodws" target="_b">{{ author }}</a> {{ timestamp }}
    </div>
  </div>
</div>

<div class="nab">
    <div class="center"><a @click="computelikes()"><button class="btn">Likes {{ likes }}</button></a></div>
    <div class="center" v-if="myblogid == 'my'"><a @click="deleteblog()"><button class="btn">Delete</button></a></div>
    <div class="center" v-if="myblogid == 'my'"><a @click="editblog()"><button class="btn">Update</button></a></div>
    <div class="center"><a @click="commentbox()"><button class="btn">Comments</button></a></div>
</div>

<section class="content">
<p>{{ content }}</p>
  
  
</section>
</template>



<script lang="ts">
export default{
  props: {
    id: {
      type: String,
      required: true,
    },
    
  },
  data(){
    return {
      title: "",
      author: "",
      content: "",
      timestamp: "",
      author_id: 0,
      image_url: "",
      likes: 0,
      blog_id: 0,




    }
  },
  mounted() {
    
    const parameter = this.id;
    fetch(`http://127.0.0.1:5000/page/${parameter}`)
    .then(response => response.json())
    .then(data => {
      
      this.title = data["blog_title"]
      this.content = data["blog_content"]
      this.timestamp = data["blog_timestamp"]
      this.image_url = data["blog_image_url"]
      this.author_id = data["blog_author_id"]
      this.likes = data["blog_likes"]
  
    
      const parameter2 = this.author_id;
      fetch(`http://127.0.0.1:5000/user/${parameter2}`)
      .then(response => response.json())
      .then(data => {
        this.author = data["user_name"]
      })
  });
    
  },
  methods:{

    computelikes() {
      this.likes = this.likes + 1;
      axios.put(`http://127.0.0.1:5000/updatelikes/${this.id}`, { likes: this.likes });

    },

    deleteblog() {
      {
        axios.delete(`http://127.0.0.1:5000/deleteblog/${this.id}`);
      }
    },

    editblog() {
      this.$router.push({ name: 'editblogview' , params: { blog_id :this.id}})
    },

    commentbox(){
      this.$router.push({ name: 'commentview' ,params: { blog_id :this.id, author: this.author}})
    }

    
  },
  computed: {
    url() {
      return `url(${this.image_url}) 100% 30%`;
    },
    myblogid() {
      
      return this.$route.query.whoseblog;
      
    }
  },
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Antic+Didone&display=swap');
@import url('https://fonts.googleapis.com/css?family=Josefin+Sans:400,400i,600,600i');
html,body{
  margin:0;
  height:120%;
  font-family: 'Josefin Sans', sans-serif;

}
body,
html {
	
	background: #cfe0e8;
}
a{
  text-decoration:none;
}
.header{
  margin-top: 25px;
  position:relative;
  overflow:hidden;
  display:flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: flex-start;
  align-content: flex-start;
  height:50vw;
  min-height:400px;
  max-height:600px;
  min-width:300px;
  color:#eee;
}
.header:after{
  content:"";
  width:100%;
  height:100%;
  position:absolute;
  bottom:0;
  left:0;
  z-index:-1;
 background: linear-gradient(to bottom, rgba(0,0,0,0.12) 40%,rgba(27,32,48,1) 100%);
}
.header:before{
  content:"";
  width:100%;
  height:200%;
  position:absolute;
  top:0;
  left:0;
    -webkit-backface-visibility: hidden;
    -webkit-transform: translateZ(0); backface-visibility: hidden;
  scale: (1.0, 1.0);
    transform: translateZ(0);
  background-size:100%;
  background-attachment:fixed;
  animation: grow 360s  linear 10ms infinite;
  transition:all 0.4s ease-in-out;
  z-index:-2;
}
.header a{
  color:#eee;
}
.menu{
  display:block;
  width:40px;
  height:30px;
  border:2px solid #fff;
  border-radius:3px;
  position:absolute;
  right:20px;
  top:20px;
  text-decoration:none;
}
.menu:after{
  content:"";
  display:block;
  width:20px;
  height:3px;
  background:#fff;
  position:absolute;
  margin:0 auto;
  top:5px;
  left:0;
  right:0;
  box-shadow:0 8px, 0 16px;
}
.logo{
  border:2px solid #fff;
  border-radius:3px;
  text-decoration:none;
  display:inline-flex;
  align-items:center;
  align-content:center;
  margin:20px;
  padding:0px 10px;
  font-weight:900;
  font-size:1.1em;
  line-height:1;
  box-sizing:border-box;
  height:40px;
}
.sides, .info{
  flex: 0 0 auto;
  width:50%;
  cursor: pointer;
}
.info{
  width:100%;
  padding:15% 10% 0 10%;
  font-family: 'Antic Didone', serif;
  font-size: 25px;
  text-align:center;
  text-shadow:0 2px 3px rgba(0,0,0,0.2);
}

.logo.u {
  position: relative;
  left: 80%;

}
.logo.m {
  position: relative;
  right: 50%;
}
  

.author{
  display:inline-block;
  width:50px;
  height:50px;
  border-radius:50%;
  background:url(https://i.imgur.com/6DLCsZcb.jpg) center no-repeat;
  background-size:cover;
  box-shadow:0 2px 3px rgba(0,0,0,0.3);
  margin-bottom:3px;
}
.info h4, .meta{
  font-size:0.7em;
}
.meta{
  font-style:italic;
}
@keyframes grow{
  0% { transform: scale(1) translateY(0px)}
  50% { transform: scale(1.2) translateY(-400px)}
}


.content{  
  padding:5% 10%;
  text-align:justify;
  color: #000;

}
.content p{
  color: #000;
  font-family: 'Antic Didone', serif;

}
.btn{
  color:#333;
  border:2px solid;
  border-radius:3px;
  text-decoration:none;
  display:inline-block;
  padding:5px 10px;
  font-weight:600;
}

.twtr{
  margin-top:100px;
}
.btn.twtr:after{content:"\1F426";
padding-left:5px;}





.nab{
    margin-top: 25px;
    margin-bottom: 25px;
    display: flex;
}

.nab button {
  margin-top: 40px;
	margin: auto;
	border-radius: 10px;
	background-color: #667292;
	box-shadow: 10px 15px 40px #36486b;
	width: 160px;
	height: 50px;
	font-size: 22.5px;
	font-family: 'Antic Didone', serif;
	color: #bccad6;
	border: none;
}

.nab button:hover {
	border: none;
	background-color: #8d9db6;
	opacity: 1;
	color: #36486b;
  cursor:pointer;
}

.nab .center {
	margin-left: auto;
	margin-right: auto;
	margin-top: auto;
	margin-bottom: auto;
	
}

.nab .btn:hover {
	transition: 0.5s ease-in-out;
	background: #8d9db6;
}

.nab button {
	--color1: #36486b;
	--color2: #bccad6;
  letter-spacing: 1.5px;
	font-family: 'Antic Didone', serif;
	text-align: center;
	font-size: 22.5px;
	background: repeating-linear-gradient(
		45deg,
		var(--color1),
		var(--color1) 30px,
		var(--color2) 30px,
		var(--color2) 60px
	);
	background-clip: text;
	color: transparent;
	-webkit-background-clip: text;
	animation: 40s linear 0s infinite move;
}

@keyframes move {
	from {
		background-position: 0px;
	}

	to {
		background-position: 1000px;
	}
}





</style>