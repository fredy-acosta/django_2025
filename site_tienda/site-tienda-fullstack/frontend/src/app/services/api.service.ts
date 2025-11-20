import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = 'http://localhost:8000/api'; // Update with your backend API URL

  constructor(private http: HttpClient) { }

  getCategories(): Observable<any> {
    return this.http.get(`${this.apiUrl}/categories/`);
  }

  getCategory(id: number): Observable<any> {
    return this.http.get(`${this.apiUrl}/categories/${id}/`);
  }

  createCategory(category: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/categories/`, category);
  }

  updateCategory(id: number, category: any): Observable<any> {
    return this.http.put(`${this.apiUrl}/categories/${id}/`, category);
  }

  deleteCategory(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/categories/${id}/`);
  }
}