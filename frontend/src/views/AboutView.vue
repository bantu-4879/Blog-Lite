<template>
  <div class="about">
    <h1>{{ post }}</h1>
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>

<script lang = 'ts'>
export default {
  data(){
    return {
      post: "u",
    }
  },
  mounted() {
    fetch("http://127.0.0.1:5000/api/test")
    .then(response => response.json())
    .then(data => {
      this.post = data["user_id"]
    })
  }

}
</script>

