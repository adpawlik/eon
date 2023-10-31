import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-hero',
  templateUrl: './hero.component.html',
  styleUrls: ['./hero.component.scss']
})
export class HeroComponent implements OnInit {

  @Input() title: string;
  @Input() description: string;
  @Input() image: string;
  @Input() hp: boolean;

  constructor() { }

  ngOnInit(): void {
  }

}
