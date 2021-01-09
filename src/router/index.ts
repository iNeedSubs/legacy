import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import About from '../views/About.vue';
import Contact from '../views/Contact.vue';
import Movie from '../views/Movie.vue';
import Show from '../views/Show.vue';
import Home from '../views/Home.vue';
import NotFound from '../views/NotFound.vue';

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
    path: '/movie/:id',
    name: 'movie',
    component: Movie
  },
  {
    path: '/show/:id',
    name: 'show',
    component: Show,
  },
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/:pathMatch(.*)*',
    component: NotFound
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
