import { LangCode } from './languages';

export interface MediaData {
  banner: string;
  poster: string;
  imdb_id: string;
  release_date: string;
  title: string;
}

// subtitles for movies
export interface Subtitle {
  download_url: string;
  language: string;
  file_name: string;
}

export interface MediaSubtitles {
  available_langs: Array<LangCode>;
  subtitles: Array<Subtitle>;
}

export enum MediaType {
  MOVIE = 'movie',
  SHOW = 'show'
}
