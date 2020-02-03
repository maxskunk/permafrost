import { Injectable } from '@angular/core';
import { HttpClient, HttpParams, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { retry, catchError, tap } from 'rxjs/operators';


@Injectable({
  providedIn: 'root'
})
export class TempUpdateService {

  apiURL = 'http://192.168.4.100:2222';
  constructor(public http: HttpClient) {
  }

  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    })
  }

  // HttpClient API get() method => Fetch employee
  public getTemp(): Observable<any> {
    let params = new HttpParams();
    // params = params.append('key', key);
    // params = params.append('wakeup', wakeup_value);
    return this.http.get<any>(this.apiURL + '/getTemp', { params: params }).pipe(
      tap( // Log the result or error
        data => {
          return data;
        },
        error => {
          return error;
        }
      )
    )
  }

  public getActualTemp(): Observable<any> {
    let params = new HttpParams();
    // params = params.append('key', key);
    // params = params.append('wakeup', wakeup_value);
    return this.http.get<any>(this.apiURL + '/getActualTemp', { params: params }).pipe(
      tap( // Log the result or error
        data => {
          return data;
        },
        error => {
          return error;
        }
      )
    )
  }

  public setTemp(temp: number): Observable<any> {
    let params = new HttpParams();
    // params = params.append('wakeup', wakeup_value);
    return this.http.get<any>(this.apiURL + '/setTemp/' + temp.toFixed(1), { params: params }).pipe(
      tap( // Log the result or error
        data => {
          return data;
        },
        error => {
          return error;
        }
      )
    )
  }

}
