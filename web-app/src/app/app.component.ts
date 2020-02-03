import { Component, OnInit } from '@angular/core';
import { TempUpdateService } from './temp-update.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  public temp: number = 0;
  public actualTemp: number = 0;

  constructor(private tempService: TempUpdateService) {

  }

  ngOnInit() {
    this.tempService.getTemp().subscribe((res: any) => {
      this.temp = Number(res);
    });
    this.getActualTemp();

    setInterval(() => {
      this.getActualTemp();
    }, 10000);
  }

  getActualTemp() {
    this.tempService.getActualTemp().subscribe((res: any) => {
      this.actualTemp = Number(res);
    });
  }

  upTemp() {
    this.temp += .1;
    this.tempService.setTemp(this.temp).subscribe((res: any) => {
      //this.temp = Number(res);
    });
  }
  downTemp() {
    this.temp -= .1;
    this.tempService.setTemp(this.temp).subscribe((res: any) => {
      //this.temp = Number(res);
    });
  }


}
