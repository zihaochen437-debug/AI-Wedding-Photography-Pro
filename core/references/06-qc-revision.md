# QC、身份升级、Scoped Revision 与重生成

## 1. 硬失败

人物不像本人、同脸/串脸/交换、明显身高/体型漂移、严重手部/人体错误、婚纱/礼服无授权改款、关键饰品错误、Scene 固定结构漂移、AI 塑料皮肤、群演继承主角脸、Revision 越界、Upscale 重绘人物、视频逐帧变脸/Morphing、严重运镜/音画错误均不能交付。

失败资产进入 `REJECTED / QUARANTINE`，禁止下游引用。

## 2. 九大一致性域

至少检查：身份/面部、人体结构、服装结构、妆发饰品、道具/接触、姿势/站位、Scene、Camera/Lighting/Color、时间连续性（视频）。

## 3. Scoped Revision

修改什么只开放什么 + 必要最小连接区域；其他已批准域冻结。越界为 `REVISION_SCOPE_VIOLATION`。

例：只修新娘右手时，锁定新娘脸、新郎、身高体型、站位动作、另一只手、婚纱、新郎礼服、Scene、Camera、Composition、Lighting、Color。

## 4. 身份升级链

正常：AB04 + AB05 + AB06。  
新娘漂移：+ AB01。  
新郎漂移：+ AB02。  
比例错误：+ AB03。  
方向持续失败：+ 对应人物该方向 1 张最佳真人原图。  
多个 Shot 持续漂移：重建对应 AB04/AB05。

增加更高权威参考时应替换冗余低权威参考，不无限叠加。

## 5. 重生成

`REGENERATION_FOLLOWS_ASSET_AUTHORITY`：重新生成不等于重新策划。继承仍有效的权威资产、Storyboard/Camera/Lighting，仅加入失败原因和本轮 Delta。

若正在重做的资产已 `REJECTED / QUARANTINE`，不得继续作为最高权威；执行 `REGENERATE_FROM_NEAREST_VALID_AUTHORITY` 回退到最近有效上游。

## 6. Upscale Diff

超分前后比较身份、五官、妆发、手、服装、饰品、Scene、Color；任何无授权重绘都失败。
