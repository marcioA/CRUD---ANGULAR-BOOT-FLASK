import 'rxjs/add/operator/map';

import { NgModule, APP_BOOTSTRAP_LISTENER } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { AlertModule } from './alert/alert.module';
import { UsuarioModule } from './usuario/usuario.module';

@NgModule({
    imports: [ BrowserModule,  AlertModule, UsuarioModule ],
    declarations: [ AppComponent ],
    bootstrap: [ AppComponent ]
})
export class AppModule{

}