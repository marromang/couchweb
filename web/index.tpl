%include('header.tpl')
<div class="content-wrapper">
  <section class="content-header">
    <h1>
      Inicio
      <small>Version 0.1</small>
    </h1>
    </br>
    <div class="col-lg-3 col-xs-6">
      <div class="small-box bg-blue">
        <div class="inner">
          <h3>{{ total }}</h3>
            <p>Servidores totales</p>
        </div>
        <div class="icon">
          <i class="ion ion-stats-bars"></i>
        </div>
      </div>
    </div>
    <div class="col-lg-3 col-xs-6">
      <div class="small-box bg-green">
        <div class="inner">
          <h3>{{ activos }}</h3>
            <p>Servidores activos</p>
        </div>
        <div class="icon">
          <i class="ion ion-stats-bars"></i>
        </div>
      </div>
    </div>
    <div class="col-lg-3 col-xs-6">
      <div class="small-box bg-red">
        <div class="inner">
          <h3>{{ inactivos }}</h3>
            <p>Servidores inactivos</p>
        </div>
        <div class="icon">
          <i class="ion ion-stats-bars"></i>
        </div>
      </div>
    </div>
  </section>
</div>
%include('footer.tpl')

