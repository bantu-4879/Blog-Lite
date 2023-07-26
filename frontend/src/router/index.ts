import { createRouter, createWebHistory } from 'vue-router'
import FeedView from '../views/FeedView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/:author',
      name: 'home',
      component: FeedView,
      props: true
    },
    {
      path: '/profile/:name',
      name: 'profile',
      component: () => import('../views/ProfileView.vue'),
      props: true
    },
    {
      path:'/post',
      name: 'post',
      component: () => import('../views/PostView.vue'),
    
    },
    {
      path:'/newblog/:author',
      name: 'newblog',
      component: () => import('../views/NewBlogView.vue'),
      props: true
    },
    {
      path:'/theblog/:id',
      name: 'theblog',
      component: () => import('../views/TheBlogView.vue'),
      props: (route) => ({
        id: route.params.id,
        whoseblog: route.query.whoseblog
      })
    },
    {
      path: '/:author',
      name: 'myblog',
      component: () => import('../views/MyBlogView.vue'),
      props: true
    },
    {
      path: '/search/:user',
      name: 'search',
      component: () => import('../views/SearchView.vue'),
      props: true
      
    },
    {
      path: '/followerview/:name/:user',
      name: 'followerview',
      component: () => import('../views/FollowerView.vue'),
      props: true
      
    },
    {
      path: '/editblogview/:blog_id',
      name: 'editblogview',
      component: () => import('../views/EditBlogView.vue'),
      props: true
      
    },
    {
      path: '/report/:author',
      name: 'report',
      component: () => import('../views/Report.vue'),
      props: true
      
    },
    {
      path: '/follower/:author',
      name: 'follower',
      component: () => import('../views/FollowersPageView.vue'),
      props: true
      
    },
    {
      path: '/commentview/:blog_id/:author',
      name: 'commentview',
      component: () => import('../views/CommentView.vue'),
      props: true
      
    },


  ]
})

export default router
