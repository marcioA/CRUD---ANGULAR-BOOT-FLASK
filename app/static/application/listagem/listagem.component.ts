import { Component } from '@angular/core';
import { Http } from '@angular/http';

@Component({
    moduleId: module.id,
    selector: 'listagem',
    templateUrl: './listagem.component.html' 
})
export class ListagemComponent { 

    usuario: Object[] = [];

    constructor(http: Http) {

        http.get('localhost:5001')
        .map(res => res.json())
            .subscribe(
                usuario => this.usuario = usuario,
                erro => console.log(erro)
            );
    }

}