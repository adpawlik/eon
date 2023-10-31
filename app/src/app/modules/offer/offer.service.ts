import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';

import { Dealer, Offer, OfferDetail, OfferList } from './offer.interface';
import {HttpParamHelper} from '../../helpers/httpParamHelper';

@Injectable({
  providedIn: 'root'
})
export class OfferService {

  constructor(private http: HttpClient) { }

  public getOffers(page = 1, sorting = {}, filters = {}): Observable<any> {
    const params = HttpParamHelper.createHttpParams(sorting, filters);
    return this.http.get<OfferList>(`${environment.apiUrl}/api/offers/?page=${page}`, {params});
  }

  public getOfferDetails(id: number) {
    return this.http.get<OfferDetail>(`${environment.apiUrl}/api/offers/${id}`);
  }

  public getPromotionalOffers() {
    return this.http.get<Offer[]>(`${environment.apiUrl}/api/offers/promotions`)
  }

  public getLatestOffers() {
    return this.http.get<Offer[]>(`${environment.apiUrl}/api/offers/latest/`)
  }

  public getDealers() {
    return this.http.get<Dealer[]>(`${environment.apiUrl}/api/dealers/`)
  }
}
