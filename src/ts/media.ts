export interface Movie {
  banner: string;
  poster: string;
  imdb_id: string;
  release_date: string;
  title: string;
}

export interface MovieSubtitle extends Movie {
  download_url: string;
  language: string;
  name: string;
}

export enum Media {
  MOVIE = 'movie',
  SHOW = 'show'
}
