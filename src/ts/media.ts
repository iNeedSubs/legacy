export interface Movie {
  imdb_id: string;
  key_visual: string;
  release_year: string;
  title: string;
}

export interface MovieSubtitle {
  download_url: string;
  language: string;
  name: string;
}

export enum Media {
  MOVIE = 'movie',
  SHOW = 'show'
}
