import { HttpParams } from '@angular/common/http';

export class HttpParamHelper {
  public static createHttpParams<T extends any[]>(...data: T): HttpParams {
    const dataToMap = this.arrayToObject(data);
    return this.arrayToParams(dataToMap);
  }

  private static arrayToObject<T extends any[],O extends Object>(data: T): O {
    return Object.assign({}, ...data);
  }
  
  private static arrayToParams<T extends Object>(data: T): HttpParams {
    let httpParams = new HttpParams();
    Object.keys(data).forEach((key) =>  (data[key] && (httpParams = httpParams.append(key, data[key]))));
    return httpParams;
  }
}
