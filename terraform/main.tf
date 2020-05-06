provider "azurerm" {
 version = "2.0.0"
 features {}
}
 
 
resource "azurerm_resource_group" "main" {
 name     = "${var.prefix}-resources"
 location = "East US 2"
}
 
resource "azurerm_virtual_network" "main" {
 name                = "${var.prefix}-network"
 address_space       = ["10.0.0.0/16"]
 location            = azurerm_resource_group.main.location
 resource_group_name = azurerm_resource_group.main.name
}
 
resource "azurerm_subnet" "internal" {
 name                 = "internal"
 resource_group_name  = azurerm_resource_group.main.name
 virtual_network_name = azurerm_virtual_network.main.name
 address_prefix       = "10.0.2.0/24"
}
 
resource "azurerm_public_ip" "main" {
 name                = "${var.prefix}-PublicIp"
 location            = azurerm_resource_group.main.location
 resource_group_name = azurerm_resource_group.main.name
 allocation_method   = "Static"
}
 
 
resource "azurerm_network_interface" "main" {
 name                = "${var.prefix}-nic"
 location            = azurerm_resource_group.main.location
 resource_group_name = azurerm_resource_group.main.name
 
 ip_configuration {
   name                          = "testconfiguration1"
   subnet_id                     = azurerm_subnet.internal.id
   private_ip_address_allocation = "Dynamic"
   public_ip_address_id          = azurerm_public_ip.main.id
 }
}
 
resource "azurerm_virtual_machine" "main" {
 name                  = "${var.prefix}-vm"
 location              = azurerm_resource_group.main.location
 resource_group_name   = azurerm_resource_group.main.name
 network_interface_ids = [azurerm_network_interface.main.id]
 vm_size               = "Standard_DS1_v2"
 
 storage_image_reference {
   publisher = "Canonical"
   offer     = "UbuntuServer"
   sku       = "16.04-LTS"
   version   = "latest"
 }
 storage_os_disk {
   name              = "myosdisk1"
   caching           = "ReadWrite"
   create_option     = "FromImage"
   managed_disk_type = "Standard_LRS"
 }
 os_profile {
   computer_name  = "hostname"
   admin_username = "craft"
   admin_password = "123456!"
 }
 os_profile_linux_config {
   disable_password_authentication = true
   ssh_keys {
     key_data = file("~/.ssh/id_rsa.pub")
     path     = "/home/craft/.ssh/authorized_keys"
   }
 
 }
 
 
 provisioner "file" {
   connection {
     host        = azurerm_public_ip.main.ip_address
     type        = "ssh"
     user        = var.admin_username
     private_key = file("~/.ssh/id_rsa")
   }
 
   source      = "~/SOFIA-project-2/terraform/keys/.ssh/id_rsa.pub"
   destination = "/home/craft/.ssh/jenkins.pub"
 }
 
 provisioner "file" {
   connection {
     host        = azurerm_public_ip.main.ip_address
     type        = "ssh"
     user        = var.admin_username
     private_key = file("~/.ssh/id_rsa")
   }
 
   source      = "~/scripts/inst_docker"
   destination = "inst_docker"
 }
 
 provisioner "file" {
   connection {
     host        = azurerm_public_ip.main.ip_address
     type        = "ssh"
     user        = var.admin_username
     private_key = file("~/.ssh/id_rsa")
   }
 
   source      = "~/scripts/inst_jenkins"
   destination = "inst_jenkins"
 }
 
}
 
 
