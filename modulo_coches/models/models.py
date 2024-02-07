# -*- coding: utf-8 -*-


from odoo import models, fields, api

class Vehiculo(models.Model):
    _name = 'gestion.vehiculo'
    _description = 'Modelo para gestionar vehículos'

    name = fields.Char(string='Nombre', required=True)
    modelo = fields.Char(string='Modelo')
    año = fields.Integer(string='Año')
    color = fields.Char(string='Color')
    matricula = fields.Char(string='Matrícula')
    precio = fields.Float(string='Precio')
    marca_id = fields.Many2one('gestion.marca', string='Marca')
    reparaciones_ids = fields.One2many('gestion.reparacion', 'vehiculo_id', string='Reparaciones')
    estado = fields.Selection([
        ('nuevo', 'Nuevo'),
        ('usado', 'Usado'),
        ('reparacion', 'En Reparación')
    ], string='Estado', default='nuevo')
    valor_estimado = fields.Float(compute='_calcular_valor_estimado', string='Valor Estimado')

    @api.depends('precio')
    def _calcular_valor_estimado(self):
        for record in self:
            record.valor_estimado = record.precio * 0.8  

class Marca(models.Model):
    _name = 'gestion.marca'
    _description = 'Modelo para las marcas de vehículos'

    name = fields.Char(string='Nombre', required=True)
    pais_origen = fields.Char(string='País de Origen')
    vehiculos_ids = fields.One2many('gestion.vehiculo', 'marca_id', string='Vehículos')

class Reparacion(models.Model):
    _name = 'gestion.reparacion'
    _description = 'Modelo para las reparaciones de vehículos'

    name = fields.Char(string='Descripción', required=True)
    fecha = fields.Date(string='Fecha de Reparación')
    costo = fields.Float(string='Costo')
    vehiculo_id = fields.Many2one('gestion.vehiculo', string='Vehículo')
    

"""
from odoo import models, fields, api

class Vehiculo(models.Model):
    _name = 'gestion.vehiculo'
    _description = 'Modelo que representa un vehículo'

    nombre = fields.Char(string='Nombre', required=True, help='Introduce el nombre del vehículo')
    marca = fields.Char(string='Marca', required=True)
    modelo = fields.Char(string='Modelo')
    año = fields.Integer(string='Año de fabricación')
    vin = fields.Char(string='VIN', size=17)
    estado = fields.Selection([
        ('0', 'Disponible'),
        ('1', 'En Servicio'),
        ('2', 'Retirado')
    ], string='Estado', default='0')

class Empleado(models.Model):
    _name = 'gestion.empleado'
    _description = 'Modelo que representa a un empleado'

    nombre = fields.Char(string='Nombre', required=True, help='Introduce el nombre completo del empleado')
    dni = fields.Char(string='DNI', required=True, size=9)
    puesto = fields.Char(string='Puesto')
    fecha_contratacion = fields.Date(string='Fecha de contratación')
"""






# class modulo_coches(models.Model):
#     _name = 'modulo_coches.modulo_coches'
#     _description = 'modulo_coches.modulo_coches'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
