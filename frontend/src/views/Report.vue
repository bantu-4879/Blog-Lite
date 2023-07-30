<template>

  <div class="rnab" v-if="send == 'no'">
    <div class="rcenter"><a @click="sendemail()"><button class="rbtn">Send Email</button></a></div> 
  </div>

  <div class="rnab" v-if="send == 'yes'">
    <div class="rcenter"><a><button class="rbtn">Mail Sent</button></a></div> 
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
  data() {
      return {
        send : 'no',
      };
  },
  
  mounted() {
    fetch(`http://127.0.0.1:5000/exportdata/${this.author}`)
    
    
  },

  methods: {
    sendemail(){
      this.send = 'yes'
      fetch(`http://127.0.0.1:5000/email_the_data`)
    }
  }
}
</script>




<style>
.rnab{
    margin: 250px 50px;
    display: flex;
}

.rnab button {
  margin-top: 40px;
	margin: auto;
	border-radius: 10px;
	background-color: #667292;
	box-shadow: 10px 15px 40px #36486b;
	width: 600px;
	height: 200px;
	font-size: 65px;
	font-family: 'Antic Didone', serif;
	color: #bccad6;
	border: none;
}

.rnab button:hover {
	border: none;
	background-color: #8d9db6;
	opacity: 1;
	color: #36486b;
  cursor:pointer;
}

.rnab .rcenter {
	margin-left: auto;
	margin-right: auto;
	margin-top: auto;
	margin-bottom: auto;
	
}

.rnab .rbtn:hover {
	transition: 0.5s ease-in-out;
	background: #8d9db6;
}

.rnab button {
	--color1: #36486b;
	--color2: #bccad6;
  letter-spacing: 1.5px;
	font-family: 'Antic Didone', serif;
	text-align: center;
	font-size: 65px;
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