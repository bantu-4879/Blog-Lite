<script setup lang="ts">
import axios from 'axios';
</script>

<template>
    <div class="card-profile">
   <div class="card_top">
      <div class="card_text">
         <h2>{{ name }}</h2>
         <p>{{ description }}</p>
      </div>
      
   </div>
   <div class="pCard_down">
      <div>
         <p>Blogs</p>
         <p>{{ blogs_count }}</p>
      </div>
      <div>
         <p>Followers</p>
         <p>{{ followers }}</p>
      </div>
      <div>
         <p>Likes</p>
         <p>{{ likes }}</p>
      </div>
   </div>
   <div class="pCard_back">
      <p>See My Latest Work Here</p>
      <a href="#"><i class="fa fa-facebook fa-2x fa-fw"></i></a>
      <a href="#"><i class="fa fa-linkedin fa-2x fa-fw"></i></a>
      <a href="#"><i class="fa fa-behance fa-2x fa-fw"></i></a> <br>
      <a href="#"><i class="fa fa-codepen fa-2x fa-fw"></i></a>
      <a href="#"><i class="fa fa-dribbble fa-2x fa-fw"></i></a>
      <a href="#"><i class="fa fa-instagram fa-2x fa-fw"></i></a>
      <p>Follow Me!</p>
   </div>
</div>
</template>



<style>
body {
  font-family: "Open Sans", sans-serif;
  background-color: #f1f9fc;
  -webkit-box-sizing: content-box;
  -moz-box-sizing: content-box;
  -ms-box-sizing: content-box;
  -o-box-sizing: content-box;
  box-sizing: content-box;
  padding: 0;
  margin: 0;
}

.card-profile {
  width: 400px;
  height: 615px;
  margin: 30px auto;
  -webkit-border-radius: 30px;
  -moz-border-radius: 30px;
  -ms-border-radius: 30px;
  -o-border-radius: 30px;
  border-radius: 30px;
  background-color: #f6fcfe;
  -webkit-box-shadow: 0px 20px 70px 0px rgba(0, 0, 0, 0.21);
  -moz-box-shadow: 0px 20px 70px 0px rgba(0, 0, 0, 0.21);
  -ms-box-shadow: 0px 20px 70px 0px rgba(0, 0, 0, 0.21);
  -o-box-shadow: 0px 20px 70px 0px rgba(0, 0, 0, 0.21);
  box-shadow: 0px 20px 70px 0px rgba(0, 0, 0, 0.21);
  position: relative;
  overflow: hidden;
}

/****************
Back
****************/

.card-profile .pCard_back {
  text-align: center;
  position: absolute;
  left: 0;
  right: 0;
  top: 50%;
  margin-top: -139px;
  font-weight: 600;
  z-index: 1;
}
.card-profile .pCard_back a {
  text-decoration: none;
}

/****************
UP
****************/

.card-profile .card_top {
  position: absolute;
  width: 100%;
  height: 437px;
  background-image: url(https://images.pexels.com/photos/1391499/pexels-photo-1391499.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500);
  background-position: 50%;
  background-size: cover;
  z-index: 3;
  text-align: center;
  -webkit-border-top-left-radius: 30px;
  -moz-border-top-left-radius: 30px;
  -ms-border-top-left-radius: 30px;
  -o-border-top-left-radius: 30px;
  border-top-left-radius: 30px;
  -webkit-border-top-right-radius: 30px;
  -moz-border-top-right-radius: 30px;
  -ms-border-top-right-radius: 30px;
  -o-border-top-right-radius: 30px;
  border-top-right-radius: 30px;
  -webkit-transition: 0.5s ease-in-out;
  -moz-transition: 0.5s ease-in-out;
  -ms-transition: 0.5s ease-in-out;
  -o-transition: 0.5s ease-in-out;
  transition: 0.5s ease-in-out;
}

.pCard_on .card_top {
  height: 100px;
  box-shadow: 0 0 30px #cfd8dc;
}

.card-profile .card_top .card_text {
  position: absolute;
  top: 319px;
  left: 0;
  right: 0;
  color: #f1f7f9;
  -webkit-transition: 0.5s ease-in-out;
  -moz-transition: 0.5s ease-in-out;
  -ms-transition: 0.5s ease-in-out;
  -o-transition: 0.5s ease-in-out;
  transition: 0.5s ease-in-out;
}

.pCard_on .card_top .card_text {
  top: 20px;
}

.card-profile .card_top .card_text h2 {
  margin: 0;
  font-size: 25px;
  font-weight: 600;
}

.card-profile .card_top .card_text p {
  margin: 0;
  font-size: 16px;
  color: #e3f1f5;
}

.card-profile .card_top .card_link {
  -webkit-border-radius: 50%;
  -moz-border-radius: 50%;
  -ms-border-radius: 50%;
  -o-border-radius: 50%;
  border-radius: 50%;
  background-color: #ed145b;
  -webkit-box-shadow: 0px 5px 24px 0px rgba(0, 0, 0, 0.43);
  -moz-box-shadow: 0px 5px 24px 0px rgba(0, 0, 0, 0.43);
  -ms-box-shadow: 0px 5px 24px 0px rgba(0, 0, 0, 0.43);
  -o-box-shadow: 0px 5px 24px 0px rgba(0, 0, 0, 0.43);
  box-shadow: 0px 5px 24px 0px rgba(0, 0, 0, 0.43);
  position: absolute;
  top: 392px;
  left: 0;
  right: 0;
  margin: auto;
  width: 88px;
  height: 88px;
  cursor: pointer;
  -webkit-transition: 0.5s ease-in-out;
  -moz-transition: 0.5s ease-in-out;
  -ms-transition: 0.5s ease-in-out;
  -o-transition: 0.5s ease-in-out;
  transition: 0.5s ease-in-out;
}

.pCard_on .card_top .card_link {
  -webkit-transform: rotate(360deg) scale(0.5);
  -moz-transform: rotate(360deg) scale(0.5);
  -ms-transform: rotate(360deg) scale(0.5);
  -o-transform: rotate(360deg) scale(0.5);
  transform: rotate(360deg) scale(0.5);
  top: 470px;
}

/****************
Down
****************/

.card-profile .pCard_down {
  background-color: #fff;
  position: absolute;
  bottom: 0px;
  width: 100%;
  height: 178px;
  z-index: 2;
  -webkit-border-bottom-left-radius: 30px;
  -moz-border-bottom-left-radius: 30px;
  -ms-border-bottom-left-radius: 30px;
  -o-border-bottom-left-radius: 30px;
  border-bottom-left-radius: 30px;
  -webkit-border-bottom-right-radius: 30px;
  -moz-border-bottom-right-radius: 30px;
  -ms-border-bottom-right-radius: 30px;
  -o-border-bottom-right-radius: 30px;
  border-bottom-right-radius: 30px;
  -webkit-transition: 0.5s ease-in-out;
  -moz-transition: 0.5s ease-in-out;
  -ms-transition: 0.5s ease-in-out;
  -o-transition: 0.5s ease-in-out;
  transition: 0.5s ease-in-out;
}

.pCard_on .pCard_down {
  height: 100px;
  -webkit-box-shadow: 0 0 30px #cfd8dc;
  -moz-box-shadow: 0 0 30px #cfd8dc;
  -ms-box-shadow: 0 0 30px #cfd8dc;
  -o-box-shadow: 0 0 30px #cfd8dc;
  box-shadow: 0 0 30px #cfd8dc;
}

.card-profile .pCard_down div {
  width: 33.333%;
  float: left;
  text-align: center;
  margin-top: 50px;
  font-size: 18px;
  -webkit-transition: 0.5s ease-in-out;
  -moz-transition: 0.5s ease-in-out;
  -ms-transition: 0.5s ease-in-out;
  -o-transition: 0.5s ease-in-out;
  transition: 0.5s ease-in-out;
}

.pCard_on .pCard_down div {
  margin-top: 10px;
}

.card-profile .pCard_down div p:first-of-type {
  color: #68818c;
  margin-bottom: 5px;
}

.card-profile .pCard_down div p:last-of-type {
  color: #334750;
  font-weight: 700;
  margin-top: 0;
}
.card-profile .pCard_back a i {
  margin: 10px;
  padding: 15px;
  -webkit-border-radius: 15px;
  -moz-border-radius: 15px;
  -ms-border-radius: 15px;
  -o-border-radius: 15px;
  border-radius: 15px;
  -webkit-transition: 0.3s ease-in-out;
  -moz-transition: 0.3s ease-in-out;
  -ms-transition: 0.3s ease-in-out;
  -o-transition: 0.3s ease-in-out;
  transition: 0.3s ease-in-out;
}

.card-profile .pCard_back a i:hover {
  -webkit-transform: scale(1.2);
  -moz-transform: scale(1.2);
  -ms-transform: scale(1.2);
  -o-transform: scale(1.2);
  transform: scale(1.2);
}

.card-profile .pCard_back a:nth-of-type(1) i {
  color: #3b5998;
  border: 2px solid #3b5998;
}

.card-profile .pCard_back a:nth-of-type(2) i {
  color: #0077b5;
  border: 2px solid #0077b5;
}

.card-profile .pCard_back a:nth-of-type(3) i {
  color: #1769ff;
  border: 2px solid #1769ff;
}

.card-profile .pCard_back a:nth-of-type(4) i {
  color: #000000;
  border: 2px solid #000000;
}

.card-profile .pCard_back a:nth-of-type(5) i {
  color: #eb5e95;
  border: 2px solid #eb5e95;
}

.card-profile .pCard_back a:nth-of-type(6) i {
  color: #3f729b;
  border: 2px solid #3f729b;
}

.card-profile .card_top a {
    position: absolute;
    width: 100%;
    height: 100%;
    margin-left: -44px;
}

.card-profile .card_top .card_link a i {
  color: white;
  font-size: 60px;
  line-height: 88px;
  display: block;
  width: 100%;
  height: 100%;

}

.card-profile .card_top a:hover {
    background-color: None;
    
}

</style>


<script lang="ts">

export default{
  props: {
    name: {
      type: String,
      required: true,
    }, 
    user:{
        type: String,
        required: true,
    }
  },
  data(){
    return {
      blogs_count: 0,
      followers: 0,
      likes: 0,
      description: ""
      

    }
  },
  mounted() {
    const name = this.name;
    fetch(`http://127.0.0.1:5000/profiledata/${name}`)
    .then(response => response.json())
    .then(data => {
      this.blogs_count = data["user_posts"]
      this.followers = data["user_followers"]
      this.likes = data["user_likes"]
      this.description = data["user_desc"]
    })
  },
  methods:{
    followingfunc(){
        const postdata = {
          user : this.user,
          name: this.name


        };
        axios.post('http://127.0.0.1:5000/followerapi', postdata)
    }
  }

}
</script>