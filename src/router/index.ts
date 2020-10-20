import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import About from '../views/About.vue';
import Contact from '../views/Contact.vue';
import Show from '../views/Show.vue';
import Movie from '../views/Movie.vue';
import Home from '../views/Home.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/about',
    name: 'about',
    component: About,
  },
  {
    path: '/contact',
    name: 'contact',
    component: Contact,
  },
  {
    path: '/show/:id',
    name: 'show',
    component: Movie,
  },
  {
    path: '/movie/:id',
    name: 'movie',
    component: Movie
  },
  {
    path: '/',
    name: 'home',
    component: Home,
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
