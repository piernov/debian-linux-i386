# Backport of Microsoft Azure Network Adapter from 6.16

## Scripts

* [Find all possible commits](log.sh)
* [Export changes](export.sh)

## Current state

### e26a0c5d828b ("net: mana: Increase the DEF_RX_BUFFERS_PER_QUEUE to 1024")
```
git cherry-pick -xs e26a0c5d828b225b88f534e2fcf10bf617f85f23
```
### c30a3f54e661 ("net: mana: Add get_link and get_link_ksettings in ethtool")
```
git cherry-pick -xs c30a3f54e661d01df2bf193398336155089dd502
```
### 6607c17c6c5e ("net: mana: Enable debugfs files for MANA device")
```
git cherry-pick -xs 6607c17c6c5e029da03a90085db22daf518232bf
```
### ae2930b0b311 ("net: mana: use ethtool string helpers")
```
git cherry-pick -xs ae2930b0b3116537e4335c4d9c1f99fa01259ac7
```
### cdd30ebb1b9f ("module: Convert symbol namespace to string literal")
Commit out of scope.
```
#git cherry-pick -xs cdd30ebb1b9f36159d66f088b61aee264e649d7a
```
### 31f1b55d5d7e ("net :mana :Request a V2 response version for MANA_QUERY_GF_STAT")
Already applied via stable: `aec9ed5663d2c4b7dd9abcdc08404e530c277b05`.
```
#git cherry-pick -xs 31f1b55d5d7e531cd827419e5d71c19f24de161c
```
### bb1e3eb57d2c ("net: mana: Fix memory leak in mana_gd_setup_irqs")
Already applied via stable: `9fda340cbfbf7909bb1c8338c204396d255f387f`.
```
#git cherry-pick -xs bb1e3eb57d2cc38951f9a9f1b8c298ced175798f
```
### 9a5beb6ca630 ("net: mana: Fix irq_contexts memory leak in mana_gd_setup_irqs")
Already applied via stable: `9f468bfed1fba8da7db13f2c55f42b7be23a9b56`.
```
#git cherry-pick -xs 9a5beb6ca6305de5c5210efab0702ea79b62eb39
```
### eaeea5028fa8 ("net: mana: Cleanup "mana" debugfs dir after cleanup of all children")
```
git cherry-pick -xs eaeea5028fa82412392d9325c44624ef8fcd1869
```
### 27315836f4bc ("net: mana: Allow tso_max_size to go up-to GSO_MAX_SIZE")
```
git cherry-pick -xs 27315836f4bcc8e4879d50dfc1fa6eb41e7952ef
```
### 47dfd7a72257 ("net: mana: Add debug logs in MANA network driver")
```
git cherry-pick -xs 47dfd7a72257e91171d56e220ea484a04df89847
```
### 29b7bb98234c ("RDMA/mana_ib: Allocate PAGE aligned doorbell index")
Already applied via stable: `c3a6c1e7b80e938be7a142a1c6b64932b2eb70d4`.
```
#git cherry-pick -xs 29b7bb98234cc287cebef9bccf638c2e3f39be71
```
### 8ef890df4031 ("net: move misc netdev_lock flavors to a separate header")
Commit out of scope.
```
#git cherry-pick -xs 8ef890df4031121a94407c84659125cbccd3fdbe
```
### 3e64bb2ae7d9 ("net: mana: cleanup mana struct after debugfs_remove()")
```
git cherry-pick -xs 3e64bb2ae7d9f2b3a8259d4d6b86ed1984d5460a
```
### 2fc8a346625e ("net: mana: Support holes in device list reply msg")
Already applied via stable: `15cc669513d65f71a063749bc161e962599209f4`.
```
#git cherry-pick -xs 2fc8a346625eb1abfe202062c7e6a13d76cde5ea
```
### c313d35f60c1 ("net: mana: Add metadata support for xdp mode")
```
git cherry-pick -xs c313d35f60c1ce20f7a43c0b6424220e697dd539
```
### 78683c25c80e ("RDMA/mana_ib: Allow registration of DMA-mapped memory in PDs")
```
git cherry-pick -xs 78683c25c80e54bf3e8015fdfb8cba2fcd03daa5
```
### 6e1b8bdcd04f ("RDMA/mana_ib: implement get_dma_mr")
```
git cherry-pick -xs 6e1b8bdcd04f4e84c924489e2f837cf620002b69
```
### 1440bdbd9c4e ("RDMA/mana_ib: helpers to allocate kernel queues")
Changes needed to `EXPORT_SYMBOL_NS`, to do missing `cdd30ebb1b9f`.
```
git cherry-pick -xs 1440bdbd9c4ee2a7461a5e547c4f7c27b4740f91
```
### bec127e45d9f ("RDMA/mana_ib: create kernel-level CQs")
```
git cherry-pick -xs bec127e45d9fd0080df679835d041615b0023ea6
```
### 7f5192a82b37 ("RDMA/mana_ib: Create and destroy UD/GSI QP")
```
git cherry-pick -xs 7f5192a82b37fd70050b7f6c5c119edf4740e8e4
```
### bd4ee700870a ("RDMA/mana_ib: UD/GSI QP creation for kernel")
```
git cherry-pick -xs bd4ee700870a732c62f32cbc102c79f75b5e88f1
```
### df91c470d9e5 ("RDMA/mana_ib: create/destroy AH")
```
git cherry-pick -xs df91c470d9e57b99e7d918dc89e1c13949f7b95e
```
### 5ec7e1c86c44 ("net/mana: fix warning in the writer of client oob")
Already applied via stable: `f5ce5628576dd8d7fdce265ee642f1b6d48cfc0b`.
```
#git cherry-pick -xs 5ec7e1c86c441c46a374577bccd9488abea30037
```
### c8017f5b4856 ("RDMA/mana_ib: UD/GSI work requests")
Changes needed to `EXPORT_SYMBOL_NS`, to do missing `cdd30ebb1b9f`.
```
git cherry-pick -xs c8017f5b4856d52c490f6517d2df7bd6eed212f3
```
### 40ebdacb4e43 ("RDMA/mana_ib: implement req_notify_cq")
Changes needed to `EXPORT_SYMBOL_NS`, to do missing `cdd30ebb1b9f`.
```
git cherry-pick -xs 40ebdacb4e433f344437b3a499d3bb5175775f2d
```
### 8001e9257eca ("RDMA/mana_ib: extend mana QP table")
```
git cherry-pick -xs 8001e9257eca23264550ff9e34598ee43a80f0f9
```
### cfef4525924e ("RDMA/mana_ib: polling of CQs for GSI/UD")
Changes needed to `EXPORT_SYMBOL_NS`, to do missing `cdd30ebb1b9f`.
```
git cherry-pick -xs cfef4525924e394005a47b02a78cde0f0318c74d
```
### 6c53bf9cff03 ("RDMA/mana_ib: indicate CM support")
```
git cherry-pick -xs 6c53bf9cff03504ad43265883ae7881f92e2e3a0
```
### bad4480934c8 ("RDMA/mana_ib: Query feature_flags bitmask from FW")
```
git cherry-pick -xs bad4480934c8227d8a03b6b76e276349506b2bfe
```
### cd3c5ddf8230 ("RDMA/mana_ib: request error CQEs when supported")
```
git cherry-pick -xs cd3c5ddf823016b0c670d1965c5d312b3cf8bb7b
```
### 79bccd746132 ("RDMA/mana_ib: Add port statistics support")
```
git cherry-pick -xs 79bccd746132afe12b8bc3785e7b74b90440060d
```
### 607a7dcf2e98 ("RDMA/mana_ib: Fix error code in probe()")
```
git cherry-pick -xs 607a7dcf2e981449a4b200f497f8ea97ddb5e13f
```
### ffd67b6b420d ("RDMA/mana_ib: Implement DMABUF MR support")
```
git cherry-pick -xs ffd67b6b420d0549e250f91eb670e98e189cd73a
```
### be35a3127d60 ("RDMA/mana_ib: Ensure variable err is initialized")
Already applied via stable: `7d25febb0e033e4c09bb4026378d35104f612f59`.
```
#git cherry-pick -xs be35a3127d60964b338da95c7bfaaf4a01b330d4
```
### 1d5c69514e74 ("RDMA/mana_ib: Use safer allocation function()")
```
git cherry-pick -xs 1d5c69514e742846ad3b8727b51b1fd46ea251fd
```
### a8445cfec101 ("net: mana: Change the function signature of mana_get_primary_netdev_rcu")
Does not apply cleanly, to do missing `cdd30ebb1b9f`.
```
git cherry-pick -xs a8445cfec101c42e9d64cdb2dac13973b22c205c
```
### bee35b7161aa ("RDMA/mana_ib: Handle net event for pointing to the current netdev")
```
git cherry-pick -xs bee35b7161aaaed9831e2f14876c374b9c566952
```
### 0c5517452422 ("RDMA/mana_ib: Fix integer overflow during queue creation")
```
git cherry-pick -xs 0c55174524227a174c1a367889cd704212d15b45
```
### fa37a8849634 ("net: mana: Switch to page pool for jumbo frames")
Already applied via stable: `34baf1cfd679bd6312f696c4277eda5085f21878`.
```
#git cherry-pick -xs fa37a8849634db2dd3545116873da8cf4b1e67c6
```
### 290e5d3c49f6 ("net: mana: Add support for Multi Vports on Bare metal")
```
git cherry-pick -xs 290e5d3c49f687c1567bde634dc33d57b0674919
```
### 7d40ccf01869 ("RDMA/mana_ib: Access remote atomic for MRs")
```
git cherry-pick -xs 7d40ccf018694ae894b37d7e849cde116eb37627
```
### 8f49682d94f3 ("RDMA/mana_ib: support of the zero based MRs")
```
git cherry-pick -xs 8f49682d94f3a12a6a3e636a07bbe57c80329d1d
```
### f1652d76f4c5 ("RDMA/mana_ib: Add support of 4M, 1G, and 2G pages")
```
git cherry-pick -xs f1652d76f4c51b5aefd14706eecbd70f05ca987a
```
### ced82fce77e9 ("net: mana: Probe rdma device in mana driver")
Does not apply cleanly, to do missing `cdd30ebb1b9f`.
```
git cherry-pick -xs ced82fce77e93315239f54caebbc88e263078e31
```
### c390828d4d7b ("RDMA/mana_ib: Add support of mana_ib for RNIC and ETH nic")
```
git cherry-pick -xs c390828d4d7b453c21c6fc0787c714db82731093
```
### d4293f96ce0b ("RDMA/mana_ib: unify mana_ib functions to support any gdma device")
```
git cherry-pick -xs d4293f96ce0b6d27d9ca13fdcd7caa135f3d2732
```
### 505cc26bcae0 ("net: mana: Add support for auxiliary device servicing events")
```
git cherry-pick -xs 505cc26bcae00699bacaee66cd50ede7a9cc89cb
```
### e0fca6f2cebf ("net: mana: Record doorbell physical address in PF mode")
Already applied via stable: `589b290d09355c54943e5e2928819d58652568ed`.
```
#git cherry-pick -xs e0fca6f2cebff539e9317a15a37dcf432e3b851a
```
### 9669ddda18fb ("net: mana: Fix warnings for missing export.h header inclusion")
```
git cherry-pick -xs 9669ddda18fbe7f1e28cd0bfc1218e746fae6c50
```
