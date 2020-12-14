import { Component, OnInit } from '@angular/core';
import { CbirService } from '../services/cbir.service';

interface HtmlInputEvent extends Event{
  target: HTMLInputElement & EventTarget;
}

@Component({
  selector: 'app-principal',
  templateUrl: './principal.component.html',
  styleUrls: ['./principal.component.css']
})
export class PrincipalComponent implements OnInit {
  
  file: File;
  imagenIngresada: String | ArrayBuffer;
  existeImagenes: boolean = false;

  img: String [] = [];
  test: String [] ;
  test2 : boolean = false;

  constructor(private cbirService: CbirService) { }

  ngOnInit(): void {
    //nada
  }

  public imagenSeleccionada(event: HtmlInputEvent): void{
    if(event.target.files && event.target.files[0]){
      this.file = <File>event.target.files[0];
      const reader = new FileReader();
      reader.onload = e => this.imagenIngresada = reader.result;
      reader.readAsDataURL(this.file);
      this.test2 = true;
    }
  }
  async cbir(){

    if(this.imagenIngresada != null){
      console.log(this.existeImagenes)
      //const a = this.cbirService.postImage(this.imagenIngresada);
      this.test = ['17.jpg','23.jpg','24.jpg','35.jpg','47.jpg','53.jpg','62.jpg'];
      //this.test = ['4.jpg','15.jpg','19.jpg','34.jpg','40.jpg','58.jpg'];
      // this.existeImagenes = true;
      // var aux
      // a.topImagenes.forEach(element => {
      //   console.log(element.nombreImagen)
      //   aux.push(element.nombreImagen)
      // });
      //   this.test = aux
    }else{
      console.log('No se ha cargado ninguna imagen')
    }
  }

}
